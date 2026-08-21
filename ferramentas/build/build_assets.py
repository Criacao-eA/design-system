# -*- coding: utf-8 -*-
"""
Pipeline de assets do Design System e-Auditoria.

1. Le os originais da pasta Links do brandbook.
2. Gera versoes otimizadas em design-system/assets/ (arquivos reais, para o time baixar).
3. Gera derivadas que nao existem (ex.: Arena Fiscal branca a partir da preta).
4. Emite manifest.json com chave -> data URI, para a montagem do catalogo.

Regra de peso: logotipo entra em PNG (precisa de alfa nitido). Foto/render 3D entra em
WebP, que comprime muito melhor sem halo. Nada acima do teto definido por categoria.
"""
import base64
import io
import json
import os
import sys

from PIL import Image

from _caminhos import DS, ASSETS, acervo

LINKS = acervo("2025", "Nova IDV", "Brandbook", "Apresentação", "Links")
OUT_MANIFEST = os.path.join(ASSETS, "manifest.json")

ASSETS = os.path.join(DS, "assets")
OUT_MANIFEST = os.path.join(ASSETS, "manifest.json")

# chave, arquivo de origem, subpasta, largura maxima do preview, formato
# formato: "png" mantem alfa nitido (logotipo); "webp" para render/foto
SPEC = [
    # --- marca e-Auditoria (originais ja sao pequenos: preserva) ---
    ("marca-horizontal-full",   "logo_horizontal.png",                              "marca", 1200, "png"),
    ("marca-horizontal-azul",   "logo_horizontal_azul.png",                         "marca", 1200, "png"),
    ("marca-horizontal-preto",  "Logotipo_2023_01-e-Auditoria-Preto.png",           "marca", 1200, "png"),
    ("marca-horizontal-branco", "Logotipo_2023_02-e-Auditoria-Branco.png",          "marca", 1200, "png"),
    ("marca-vertical-azul",     "Logotipo_2023_06-e-Auditoria-Vertical-Azul.png",   "marca",  600, "png"),
    ("marca-vertical-preto",    "Logotipo_2023_04-e-Auditoria-Vertical-Preto.png",  "marca",  600, "png"),
    ("marca-vertical-branco",   "Logotipo_2023_05-e-Auditoria-Vertical-Branco.png", "marca",  600, "png"),
    ("simbolo-preto",           "E-simbolo.png",                                    "marca",  512, "png"),
    # --- sub-marcas ---
    ("arena-colorido",          "20251105_IDV_Arena-Fiscal-colorido.png",           "marca",  900, "png"),
    ("arena-preto",             "20251105_IDV_Arena-Fiscal.png",                    "marca",  900, "png"),
    ("imersao-colorido",        "imersão-eA.png",                                   "marca",  900, "png"),
    # --- mascotes ---
    ("ebot-corpo",              "ebot 1.png",                                       "mascotes", 640, "webp"),
    ("ebot-perfil",             "ebot foto de perfil.png",                          "mascotes", 480, "webp"),
    ("ebot-perfil2",            "ebot foto de perfil_2.png",                        "mascotes", 480, "webp"),
    ("incendiaria-corpo",       "incendiarios.png",                                 "mascotes", 620, "webp"),
    # --- vidro (referencia) ---
    ("vidro-cubo",              "Cube6 - Transparent.png",                          "vidro", 520, "webp"),
    ("vidro-onda",              "AdobeStock_1319700922.png",                        "vidro", 520, "webp"),
    ("vidro-grafico",           "AdobeStock_1374460825.png",                        "vidro", 520, "webp"),
    ("vidro-lamina",            "AdobeStock_1391673595.png",                        "vidro", 520, "webp"),
    ("vidro-camadas",           "AdobeStock_1393073383.png",                        "vidro", 520, "webp"),
    ("vidro-arco",              "AdobeStock_1458388906 1.png",                      "vidro", 520, "webp"),
    ("vidro-fita1",             "AdobeStock_1458388957 1.png",                      "vidro", 520, "webp"),
    ("vidro-fita2",             "AdobeStock_1499505904 1.png",                      "vidro", 520, "webp"),
    # --- icones 3D (referencia) ---
    ("icone3d-cursor",          "AdobeStock_974046669.png",                         "icones", 420, "webp"),
    ("icone3d-1",               "AdobeStock_1060616988.png",                        "icones", 420, "webp"),
    ("icone3d-2",               "AdobeStock_1060617906.png",                        "icones", 420, "webp"),
    ("icone3d-explod",          "Exploding head.png",                               "icones", 420, "webp"),
    ("icone3d-p2p",             "Peer To Peer .png",                                "icones", 420, "webp"),
    ("icone3d-stock",           "Stock And Dividens.png",                           "icones", 420, "webp"),
    ("icone3d-woozy",           "Woozy face.png",                                   "icones", 420, "webp"),
    # --- backgrounds (referencia) ---
    ("bg-rectangle",            "Rectangle.png",                                    "backgrounds", 560, "webp"),
    ("bg-02",                   "02.png",                                           "backgrounds", 560, "webp"),
    ("bg-aulao1",               "BG Aulão eA.png",                                  "backgrounds", 560, "webp"),
    ("bg-aulao2",               "BG Aulão eA_2.png",                                "backgrounds", 560, "webp"),
    ("bg-crossell",             "BG_LP_crossell_tributação.jpg",                    "backgrounds", 560, "webp"),
    ("bg-infografico",          "BG_LP_infografico.jpg",                            "backgrounds", 560, "webp"),
    ("bg-vidroroxo",            "BG-vidro-roxo.png",                                "backgrounds", 560, "webp"),
    ("bg-capa",                 "Brandbook_capa.png",                               "backgrounds", 560, "webp"),
    ("bg-image1",               "Image (1).png",                                    "backgrounds", 560, "webp"),
    ("bg-imagem2",              "Imagem2.png",                                      "backgrounds", 560, "webp"),
]


def recolor_alpha(img, rgb):
    """Mantem o alfa e pinta tudo de uma cor so. Usado para gerar versao branca/preta."""
    img = img.convert("RGBA")
    solid = Image.new("RGBA", img.size, rgb + (255,))
    solid.putalpha(img.getchannel("A"))
    return solid


def fit(img, max_w):
    if img.width <= max_w:
        return img
    h = round(img.height * max_w / img.width)
    return img.resize((max_w, h), Image.LANCZOS)


def encode(img, fmt, teto_kb):
    """Serializa buscando a maior qualidade que cabe no teto."""
    if fmt == "png":
        buf = io.BytesIO()
        img.save(buf, "PNG", optimize=True)
        data = buf.getvalue()
        if len(data) <= teto_kb * 1024:
            return data, "image/png"
        fmt = "webp"  # PNG estourou: cai para webp sem perda de alfa
    for q in (86, 80, 74, 68, 60, 52, 44):
        buf = io.BytesIO()
        img.save(buf, "WEBP", quality=q, method=6)
        data = buf.getvalue()
        if len(data) <= teto_kb * 1024:
            return data, "image/webp"
    return data, "image/webp"


TETO = {"marca": 90, "mascotes": 110, "vidro": 60, "icones": 45, "backgrounds": 60}

manifest = {}
relatorio = []
faltando = []

for chave, arquivo, sub, max_w, fmt in SPEC:
    origem = os.path.join(LINKS, arquivo)
    if not os.path.exists(origem):
        faltando.append((chave, arquivo))
        continue
    img = Image.open(origem).convert("RGBA")
    dim_orig = f"{img.width}x{img.height}"
    img = fit(img, max_w)
    data, mime = encode(img, fmt, TETO[sub])

    destino_dir = os.path.join(ASSETS, sub)
    os.makedirs(destino_dir, exist_ok=True)
    ext = "png" if mime == "image/png" else "webp"
    with open(os.path.join(destino_dir, f"{chave}.{ext}"), "wb") as fh:
        fh.write(data)

    manifest[chave] = f"data:{mime};base64," + base64.b64encode(data).decode("ascii")
    relatorio.append((chave, dim_orig, f"{img.width}x{img.height}", ext, round(len(data) / 1024, 1)))

# ---- derivadas que nao existem no material de origem ----
derivadas = [
    # (chave nova, arquivo base preto, cor alvo, subpasta, largura, teto)
    ("arena-branco", "20251105_IDV_Arena-Fiscal.png", (255, 255, 255), "marca", 900),
]
for chave, base_arq, cor, sub, max_w in derivadas:
    origem = os.path.join(LINKS, base_arq)
    if not os.path.exists(origem):
        faltando.append((chave, base_arq))
        continue
    img = recolor_alpha(Image.open(origem), cor)
    img = fit(img, max_w)
    data, mime = encode(img, "png", TETO[sub])
    ext = "png" if mime == "image/png" else "webp"
    with open(os.path.join(ASSETS, sub, f"{chave}.{ext}"), "wb") as fh:
        fh.write(data)
    manifest[chave] = f"data:{mime};base64," + base64.b64encode(data).decode("ascii")
    relatorio.append((chave, "derivada", f"{img.width}x{img.height}", ext, round(len(data) / 1024, 1)))

with open(OUT_MANIFEST, "w", encoding="utf-8") as fh:
    json.dump(manifest, fh)

total = sum(r[4] for r in relatorio)
print(f"{'chave':<24} {'origem':>11} {'preview':>11} {'fmt':>5} {'KB':>7}")
print("-" * 64)
for r in sorted(relatorio, key=lambda x: -x[4]):
    print(f"{r[0]:<24} {r[1]:>11} {r[2]:>11} {r[3]:>5} {r[4]:>7}")
print("-" * 64)
print(f"{len(relatorio)} assets | total embutido: {round(total/1024,2)} MB")
if faltando:
    print("\nAUSENTES:")
    for c, a in faltando:
        print(f"  {c}  <- {a}")
