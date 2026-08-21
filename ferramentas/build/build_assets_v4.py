# -*- coding: utf-8 -*-
"""Assets das sub-marcas (v4). Acrescenta ao manifest existente."""
import base64, io, json, os
from PIL import Image

from _caminhos import DS, ASSETS, MANIFEST, acervo

# raiz do acervo de artes originais (fora do repositório) — ver EA_ACERVO
B = acervo()

IMERSAO_A = os.path.join(B, r"2025\Auloes\Imersao eA")
IMERSAO_M = os.path.join(B, r"2025\Material_rico\eA Imersão")
AULAO_1X = os.path.join(B, r"2025\Auloes\Aulão eA\1x")
AULAO = os.path.join(B, r"2025\Auloes\Aulão eA")
SPED = os.path.join(B, r"2025\Auloes\Aulao Corretor do SPED")
JOGO_2X = os.path.join(B, r"2026\O Jogo da Reforma\2x")
JOGO = os.path.join(B, r"2026\O Jogo da Reforma")
RADAR = os.path.join(B, r"2026\IDV\Radar Tributario\2x")
PREMIA = os.path.join(B, r"2025\Nova IDV\PremIA")
AUTORES = os.path.join(B, r"2025\Nova IDV\Autores Tributarios")
JORNADA = os.path.join(B, r"2026\Landing Pages\Jornada do Especialista")
PARC = os.path.join(B, r"2026\Landing Pages\lp-parcerias-ea")

# chave, caminho, subpasta, largura max, formato preferido, teto KB
SPEC = [
    # Imersao — logotipo em PNG (precisa de alfa nitido), resto em WebP
    ("imersao-logo",             os.path.join(IMERSAO_M, r"1x\imersão eA.png"),        "imersao", 900, "png", 70),
    ("imersao-online-gratuito",  os.path.join(IMERSAO_M, r"1x\online e gratuito.png"), "imersao", 700, "png", 50),
    ("imersao-bg-lp",            os.path.join(IMERSAO_A, "BG_Lp.png"),                 "imersao", 620, "webp", 55),
    ("imersao-bg1",              os.path.join(IMERSAO_M, "bg 2.png"),                  "imersao", 560, "webp", 45),
    ("imersao-bg2",              os.path.join(IMERSAO_M, "bg 3.png"),                  "imersao", 560, "webp", 45),
    ("imersao-bg3",              os.path.join(IMERSAO_M, "bg 5.png"),                  "imersao", 560, "webp", 45),
    ("imersao-story1",           os.path.join(IMERSAO_A, "Imersao eA - Story 01.png"), "imersao", 420, "webp", 45),
    ("imersao-story2",           os.path.join(IMERSAO_A, "Imersao eA - Story 03.png"), "imersao", 420, "webp", 45),
    ("imersao-feed",             os.path.join(IMERSAO_A, "Imersao-eA_Feed-MF.png"),    "imersao", 480, "webp", 50),
    ("imersao-aula1",            os.path.join(IMERSAO_A, "Aula 1 _ Bruno Viana.png"),  "imersao", 480, "webp", 45),
    ("imersao-aula2",            os.path.join(IMERSAO_A, "Aula 2 _ Nathalia Pizelli.png"), "imersao", 480, "webp", 45),
    # Aulao
    ("aulao-logo-azul",     os.path.join(AULAO_1X, "logo-bg-azul.png"),     "aulao", 700, "png", 50),
    ("aulao-logo-branco",   os.path.join(AULAO_1X, "logo-bg-branco.png"),   "aulao", 700, "png", 50),
    ("aulao-logo-preto",    os.path.join(AULAO_1X, "logo-bg-preto.png"),    "aulao", 700, "png", 50),
    ("aulao-aviso",         os.path.join(AULAO_1X, "aviso.png"),            "aulao", 320, "png", 35),
    ("aulao-bg-tema",       os.path.join(AULAO_1X, "bg-tema.png"),          "aulao", 620, "webp", 45),
    ("aulao-bg-degrade",    os.path.join(AULAO_1X, "bg_degrade.png"),       "aulao", 620, "webp", 40),
    ("aulao-tema",          os.path.join(AULAO_1X, "tema.png"),             "aulao", 420, "png", 35),
    ("aulao-tema-data",     os.path.join(AULAO_1X, "tema-data.png"),        "aulao", 420, "png", 35),
    ("aulao-tema-data-azul",os.path.join(AULAO_1X, "tema-data-azul.png"),   "aulao", 420, "png", 35),
    ("aulao-social1",       os.path.join(AULAO, "Thumbnail_aulao_novo-KV_com-data.png"), "aulao", 520, "webp", 50),
    ("aulao-social2",       os.path.join(AULAO, "Feed_Teaser-aulao.png"),   "aulao", 480, "webp", 50),
    ("aulao-social3",       os.path.join(AULAO, "Story_Teaser-aulao.png"),  "aulao", 400, "webp", 45),
    ("aulao-sped1",         os.path.join(SPED, "Thumbnail_aulao_com-data_como-corrigir-SPED_em-minutos.png"), "aulao", 520, "webp", 50),
    ("aulao-sped2",         os.path.join(SPED, "2025-05-23_MR_Aulão_corretor-do-SPED_Miolo-Blog.png"), "aulao", 520, "webp", 45),
    # Jogo
    ("jogo-azul",   os.path.join(JOGO_2X, "Jogo da Contabilidade_azul@2x.png"),        "jogo", 700, "png", 55),
    ("jogo-claro",  os.path.join(JOGO_2X, "Jogo da Contabilidade_fundo claro@2x.png"), "jogo", 700, "png", 55),
    ("jogo-escuro", os.path.join(JOGO_2X, "Jogo da Contabilidade_fundo escuro@2x.png"),"jogo", 700, "png", 55),
    ("jogo-thumb1", os.path.join(JOGO, "202600303-O Jogo da Reforma-thumb-vertical-episodio 17.png"), "jogo", 420, "webp", 50),
    ("jogo-thumb2", os.path.join(JOGO, "20260119_O-jogo-da-reforma-thumbnail-epiodio-11.png"), "jogo", 520, "webp", 50),
    ("jogo-thumb3", os.path.join(JOGO, "20260126_O-jogo-da-reforma-tela-ao-vivo-em-instantes_epi-12.png"), "jogo", 520, "webp", 50),
    # Radar
    ("radar-p1", os.path.join(RADAR, "Prancheta 1@2x.png"), "radar", 620, "png", 55),
    ("radar-p2", os.path.join(RADAR, "Prancheta 2@2x.png"), "radar", 620, "png", 55),
    ("radar-p4", os.path.join(RADAR, "Prancheta 4@2x.png"), "radar", 620, "png", 55),
    ("radar-p6", os.path.join(RADAR, "Prancheta 6@2x.png"), "radar", 620, "png", 55),
    ("radar-idv", os.path.join(RADAR, "IDV_Radar-Tributario.png"), "radar", 560, "webp", 50),
    ("radar-bg", os.path.join(RADAR, "Background_Radar Tributario@2x.png"), "radar", 560, "webp", 45),
    ("radar-bg-feed", os.path.join(RADAR, "Background Feed_Radar Tributario@2x.png"), "radar", 480, "webp", 45),
    ("radar-bg-story", os.path.join(RADAR, "Background Story_Radar Tributario@2x.png"), "radar", 400, "webp", 45),
    ("radar-post-feed", os.path.join(RADAR, "Modelo postagem feed_Radar Trbutario 3x4@2x.png"), "radar", 460, "webp", 50),
    ("radar-post-story", os.path.join(RADAR, "Modelo postagem feed_Radar Trbutario 9x16@2x.png"), "radar", 400, "webp", 50),
    # PremIA / Autores
    ("premia-teams", os.path.join(PREMIA, "250908-PremIA-teams-1920x1080.png"), "premia", 620, "webp", 55),
    ("autores-cartaz", os.path.join(AUTORES, "250723_autores-tributarios_cartaz-a3_nath.png"), "premia", 460, "webp", 50),
    ("autores-teams", os.path.join(AUTORES, "250724_autores-tributarios_teams.png"), "premia", 620, "webp", 55),
    ("autores-premios", os.path.join(AUTORES, "250908-autores-tributarios-premios-especiais-teams-1920x1080.png"), "premia", 620, "webp", 55),
    ("autores-mes-a", os.path.join(AUTORES, "Autor tributário do mês.png"), "premia", 560, "webp", 50),
    ("autores-mes-b", os.path.join(AUTORES, "Autora tributária do mês.png"), "premia", 560, "webp", 50),
    # Jornada / Parcerias
    ("jornada-bg", os.path.join(JORNADA, "background.png"), "jornada", 620, "webp", 50),
    ("parceiro-badge", os.path.join(PARC, "logo-badge.png"), "parcerias", 520, "png", 55),
]


def fit(img, w):
    if img.width <= w:
        return img
    return img.resize((w, round(img.height * w / img.width)), Image.LANCZOS)


def encode(img, fmt, teto):
    if fmt == "png":
        buf = io.BytesIO(); img.save(buf, "PNG", optimize=True)
        if len(buf.getvalue()) <= teto * 1024:
            return buf.getvalue(), "image/png"
    for q in (88, 82, 76, 70, 62, 54, 46):
        buf = io.BytesIO(); img.save(buf, "WEBP", quality=q, method=6)
        if len(buf.getvalue()) <= teto * 1024:
            return buf.getvalue(), "image/webp"
    return buf.getvalue(), "image/webp"


d = json.load(open(MANIFEST, encoding="utf-8")) if os.path.exists(MANIFEST) else {}
antes = len(d)
rel, faltando = [], []

for chave, origem, sub, w, fmt, teto in SPEC:
    if not os.path.exists(origem):
        faltando.append((chave, os.path.basename(origem))); continue
    img = Image.open(origem).convert("RGBA")
    dim = f"{img.width}x{img.height}"
    img = fit(img, w)
    data, mime = encode(img, fmt, teto)
    destino = os.path.join(ASSETS, sub); os.makedirs(destino, exist_ok=True)
    ext = "png" if mime == "image/png" else "webp"
    open(os.path.join(destino, f"{chave}.{ext}"), "wb").write(data)
    d[chave] = f"data:{mime};base64," + base64.b64encode(data).decode()
    rel.append((chave, dim, f"{img.width}x{img.height}", ext, round(len(data)/1024, 1)))

json.dump(d, open(MANIFEST, "w", encoding="utf-8"))
peso = sum(len(v) for v in d.values())/1024/1024
print(f"{'chave':<24}{'origem':>12}{'preview':>11}{'fmt':>6}{'KB':>7}")
print("-" * 62)
for r in sorted(rel, key=lambda x: -x[4])[:14]:
    print(f"{r[0]:<24}{r[1]:>12}{r[2]:>11}{r[3]:>6}{r[4]:>7}")
print("-" * 62)
print(f"+{len(rel)} assets (novo total {len(d)}, era {antes}) | {sum(r[4] for r in rel)/1024:.2f} MB nesta leva | manifest {peso:.2f} MB")
if faltando:
    print("\nAUSENTES:")
    for c, a in faltando: print(f"  {c:<24} <- {a}")
