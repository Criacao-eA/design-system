# -*- coding: utf-8 -*-
"""
Verificacao independente dos SVGs tracados.

Nao confia no relatorio do agente: rasteriza o SVG a partir dos proprios paths
(sao polilinhas M/L/Z, sem curvas), aplica regra evenodd via XOR de poligonos,
e compara com a mascara alfa do PNG original. Sai com a taxa de divergencia real
e grava um comparativo visual lado a lado.
"""
import os
import re

from PIL import Image, ImageChops, ImageDraw

from _caminhos import MARCA, SCRATCH, acervo

LINKS = acervo("2025", "Nova IDV", "Brandbook", "Apresentação", "Links")
OUT = os.path.join(SCRATCH, "verificar_svg")


PARES = [
    ("ea-simbolo.svg",   "E-simbolo.png"),
    ("ea-horizontal.svg","Logotipo_2023_01-e-Auditoria-Preto.png"),
    ("ea-vertical.svg",  "Logotipo_2023_04-e-Auditoria-Vertical-Preto.png"),
    ("arena-fiscal.svg", "20251105_IDV_Arena-Fiscal.png"),
    ("imersao-ea.svg",   "imersão-eA.png"),
]

NUM = re.compile(r"-?\d*\.?\d+")


def ler_svg(caminho):
    with open(caminho, encoding="utf-8") as fh:
        txt = fh.read()
    vb = re.search(r'viewBox="([^"]+)"', txt)
    vx, vy, vw, vh = [float(n) for n in NUM.findall(vb.group(1))]
    ds = re.findall(r'\sd="([^"]+)"', txt)
    return (vx, vy, vw, vh), ds


def subpaths(d):
    """Quebra um atributo d em listas de pontos. Suporta M/L/Z absolutos."""
    saida, atual = [], []
    for cmd, corpo in re.findall(r"([MLZmlz])([^MLZmlz]*)", d):
        nums = [float(n) for n in NUM.findall(corpo)]
        c = cmd.upper()
        if c == "Z":
            if len(atual) >= 3:
                saida.append(atual)
            atual = []
            continue
        pares = list(zip(nums[0::2], nums[1::2]))
        if c == "M":
            if len(atual) >= 3:
                saida.append(atual)
            atual = list(pares)
        else:
            atual.extend(pares)
    if len(atual) >= 3:
        saida.append(atual)
    return saida


def rasterizar(caminho_svg, larg, alt):
    (vx, vy, vw, vh), ds = ler_svg(caminho_svg)
    sx, sy = larg / vw, alt / vh
    acumulado = Image.new("1", (larg, alt), 0)
    for d in ds:
        for pts in subpaths(d):
            camada = Image.new("1", (larg, alt), 0)
            ImageDraw.Draw(camada).polygon(
                [((x - vx) * sx, (y - vy) * sy) for x, y in pts], fill=1)
            # evenodd: sobreposicao vira buraco
            acumulado = ImageChops.logical_xor(acumulado, camada)
    return acumulado


def mascara_original(caminho_png, larg, alt):
    img = Image.open(caminho_png).convert("RGBA")
    alfa = img.getchannel("A")
    if alfa.getextrema()[1] == 0:
        alfa = img.convert("L").point(lambda v: 255 - v)
    bbox = alfa.point(lambda v: 255 if v > 128 else 0).getbbox()
    if bbox:
        alfa = alfa.crop(bbox)
    return alfa.resize((larg, alt), Image.LANCZOS).point(lambda v: 1 if v > 128 else 0, "1")


print(f"{'svg':<22}{'KB':>6}{'paths':>7}{'divergencia':>13}   veredito")
print("-" * 62)
tiras = []
for svg_nome, png_nome in PARES:
    p_svg = os.path.join(MARCA, svg_nome)
    p_png = os.path.join(LINKS, png_nome)
    if not (os.path.exists(p_svg) and os.path.exists(p_png)):
        print(f"{svg_nome:<22} AUSENTE")
        continue
    L = 600
    orig_img = Image.open(p_png)
    alt = max(60, round(L * orig_img.height / orig_img.width))
    (_, _, vw, vh), ds = ler_svg(p_svg)
    alt_svg = max(60, round(L * vh / vw))
    alt = alt_svg  # compara na proporcao do SVG (que e o bbox apertado)

    a = rasterizar(p_svg, L, alt)
    b = mascara_original(p_png, L, alt)
    dif = ImageChops.logical_xor(a, b)
    n_dif = sum(dif.point(lambda v: 1 if v else 0).getdata())
    pct = 100.0 * n_dif / (L * alt)
    kb = round(os.path.getsize(p_svg) / 1024, 1)
    veredito = "OK" if pct < 1.0 else ("aceitavel" if pct < 3.0 else "REVISAR")
    print(f"{svg_nome:<22}{kb:>6}{len(ds):>7}{pct:>12.2f}%   {veredito}")

    tira = Image.new("RGB", (L, alt * 3 + 16), (136, 153, 170))
    tira.paste(a.convert("RGB").point(lambda v: 255 - v * 255), (0, 0))
    tira.paste(b.convert("RGB").point(lambda v: 255 - v * 255), (0, alt + 8))
    tira.paste(dif.convert("RGB").point(lambda v: v * 255), (0, alt * 2 + 16))
    tiras.append((svg_nome, tira))

if tiras:
    larg_t = max(t.width for _, t in tiras)
    alt_t = sum(t.height + 24 for _, t in tiras)
    folha = Image.new("RGB", (larg_t, alt_t), (136, 153, 170))
    y = 0
    d = ImageDraw.Draw(folha)
    for nome, t in tiras:
        folha.paste(t, (0, y))
        d.text((6, y + t.height + 5), f"{nome}  (SVG / original / diferenca)", fill=(255, 0, 255))
        y += t.height + 24
    folha.save(os.path.join(OUT, "verificacao-svg.png"))
    print("\ncomparativo visual -> verificacao-svg.png")
