# -*- coding: utf-8 -*-
"""
Reduz o peso do manifest sem tirar nada do catalogo.

O problema: 92 imagens embutidas como data URI levaram a pagina a 5,7 MB. Data URI
em base64 ainda infla ~33%. A saida nao e remover conteudo, e reencodar com um
orcamento por PAPEL da imagem:

- logotipo  : precisa de alfa nitido e le-se em tamanho medio -> PNG, teto baixo
- referencia: e miniatura de galeria, ninguem le detalhe -> WebP agressivo
- fundo     : e textura, tolera muita compressao -> WebP muito agressivo

Os arquivos em disco continuam nos tamanhos originais; so o que vai EMBUTIDO encolhe.
"""
import base64, io, json, os, re
from PIL import Image

from _caminhos import DS, ASSETS, MANIFEST

ASSETS = os.path.join(DS, "assets")
MANIFEST = os.path.join(ASSETS, "manifest.json")

# papel -> (largura maxima embutida, teto em KB)
ORCAMENTO = {
    "logo":       (620, 34),
    "referencia": (400, 20),
    "fundo":      (420, 16),
}

LOGO = re.compile(r"(marca-|simbolo|arena-|imersao-logo|imersao-online|aulao-logo|"
                  r"jogo-(azul|claro|escuro)|radar-p\d|parceiro-badge|aulao-tema|aulao-aviso)")
FUNDO = re.compile(r"(^bg-|-bg|bg\d|fundo|jornada-bg|radar-bg)")


def papel(chave):
    if LOGO.search(chave):
        return "logo"
    if FUNDO.search(chave):
        return "fundo"
    return "referencia"


def achar(chave):
    for sub in os.listdir(ASSETS):
        d = os.path.join(ASSETS, sub)
        if not os.path.isdir(d):
            continue
        for ext in ("png", "webp"):
            p = os.path.join(d, f"{chave}.{ext}")
            if os.path.exists(p):
                return p
    return None


d = json.load(open(MANIFEST, encoding="utf-8"))
antes = sum(len(v) for v in d.values()) / 1024 / 1024
mudou, faltou = 0, []

for chave in list(d.keys()):
    p = achar(chave)
    if not p:
        faltou.append(chave)
        continue
    pap = papel(chave)
    largura, teto = ORCAMENTO[pap]
    img = Image.open(p).convert("RGBA")
    if img.width > largura:
        img = img.resize((largura, round(img.height * largura / img.width)), Image.LANCZOS)

    melhor = None
    if pap == "logo":
        buf = io.BytesIO(); img.save(buf, "PNG", optimize=True)
        if len(buf.getvalue()) <= teto * 1024:
            melhor = (buf.getvalue(), "image/png")
    if melhor is None:
        # busca binaria na qualidade: 4 tentativas em vez de 7, e method=4
        # (method=6 e ~4x mais lento para ~2% de ganho — nao compensa em 92 imagens)
        lo, hi, achou = 30, 86, None
        for _ in range(4):
            q = (lo + hi) // 2
            buf = io.BytesIO(); img.save(buf, "WEBP", quality=q, method=4)
            if len(buf.getvalue()) <= teto * 1024:
                achou = buf.getvalue(); lo = q + 1
            else:
                hi = q - 1
            if lo > hi:
                break
        if achou is None:
            buf = io.BytesIO(); img.save(buf, "WEBP", quality=30, method=4)
            achou = buf.getvalue()
        melhor = (achou, "image/webp")

    novo = f"data:{melhor[1]};base64," + base64.b64encode(melhor[0]).decode()
    if len(novo) < len(d[chave]):
        d[chave] = novo
        mudou += 1

json.dump(d, open(MANIFEST, "w", encoding="utf-8"))
depois = sum(len(v) for v in d.values()) / 1024 / 1024
print(f"{len(d)} chaves | {mudou} reencodadas | {antes:.2f} MB -> {depois:.2f} MB embutidos")
if faltou:
    print("sem arquivo em disco (mantidas como estavam):", ", ".join(faltou[:8]))
