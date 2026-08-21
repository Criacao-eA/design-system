# -*- coding: utf-8 -*-
"""
Gera PNG de alta resolucao a partir dos SVGs tracados.

Isto resolve um problema real do material de origem: os PNGs oficiais do logotipo
sao pequenos (641x75 o horizontal, 139x148 o vertical). Nao da para "aumentar" um
raster sem perder. Com o vetor, a alta resolucao passa a existir de verdade.

Rasteriza com supersampling 4x e downsample LANCZOS, o que da borda limpa sem
depender de biblioteca de SVG.
"""
import base64
import io
import json
import os
import re

from PIL import Image, ImageChops, ImageDraw

from _caminhos import MARCA, MANIFEST


NUM = re.compile(r"-?\d*\.?\d+")
SS = 4  # supersampling

CORES = {
    "azul":   (43, 46, 111),    # #2B2E6F — azul oficial do logotipo
    "preto":  (5, 6, 52),       # #050634 — navy da marca
    "branco": (255, 255, 255),
}

# svg -> (prefixo do arquivo, larguras a gerar)
ALVOS = {
    "ea-horizontal": ("ea-logo-horizontal", [1000, 2000, 4000]),
    "ea-vertical":   ("ea-logo-vertical",   [600, 1200, 2400]),
    "ea-simbolo":    ("ea-simbolo",         [512, 1024, 2048]),
    "arena-fiscal":  ("arena-fiscal",       [1000, 2000]),
    "imersao-ea":    ("imersao-ea",         [1000, 2000]),
}


def ler_svg(caminho):
    with open(caminho, encoding="utf-8") as fh:
        txt = fh.read()
    vb = re.search(r'viewBox="([^"]+)"', txt)
    vx, vy, vw, vh = [float(n) for n in NUM.findall(vb.group(1))]
    return (vx, vy, vw, vh), re.findall(r'\sd="([^"]+)"', txt)


def subpaths(d):
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


def mascara(caminho_svg, larg):
    (vx, vy, vw, vh), ds = ler_svg(caminho_svg)
    alt = max(1, round(larg * vh / vw))
    W, H = larg * SS, alt * SS
    sx, sy = W / vw, H / vh
    acc = Image.new("1", (W, H), 0)
    for d in ds:
        for pts in subpaths(d):
            camada = Image.new("1", (W, H), 0)
            ImageDraw.Draw(camada).polygon(
                [((x - vx) * sx, (y - vy) * sy) for x, y in pts], fill=1)
            acc = ImageChops.logical_xor(acc, camada)
    return acc.convert("L").resize((larg, alt), Image.LANCZOS), alt


with open(MANIFEST, encoding="utf-8") as fh:
    manifest = json.load(fh)

print(f"{'arquivo':<38}{'px':>12}{'KB':>8}")
print("-" * 58)
gerados = 0
for chave, (prefixo, larguras) in ALVOS.items():
    p = os.path.join(MARCA, chave + ".svg")
    if not os.path.exists(p):
        print(f"{chave:<38}  SVG AUSENTE")
        continue
    for larg in larguras:
        alfa, alt = mascara(p, larg)
        for nome_cor, rgb in CORES.items():
            img = Image.new("RGBA", (larg, alt), rgb + (0,))
            img.putalpha(alfa)
            nome = f"{prefixo}-{nome_cor}-{larg}w.png"
            destino = os.path.join(MARCA, nome)
            img.save(destino, "PNG", optimize=True)
            gerados += 1
            if larg == larguras[-1]:
                print(f"{nome:<38}{f'{larg}x{alt}':>12}"
                      f"{round(os.path.getsize(destino)/1024,1):>8}")
            # o maior de cada cor entra no manifest como download de alta
            if larg == larguras[-1]:
                buf = io.BytesIO()
                img.save(buf, "PNG", optimize=True)
                manifest[f"{prefixo}-{nome_cor}-alta"] = (
                    "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode("ascii"))

with open(MANIFEST, "w", encoding="utf-8") as fh:
    json.dump(manifest, fh)

peso = sum(len(v) for v in manifest.values()) / 1024 / 1024
print("-" * 58)
print(f"{gerados} PNGs gerados | manifest agora com {len(manifest)} chaves | {peso:.2f} MB embutidos")
