# -*- coding: utf-8 -*-
"""
Prepara os SVGs oficiais do Programa de Parcerias para uso inline no catalogo.

Problema: os seis arquivos foram exportados do Illustrator e TODOS usam as mesmas
classes (.cls-1, .cls-2...) com cores diferentes. Inline na mesma pagina, a ultima
regra vence e todos os logotipos ficam com a cor do ultimo. E um bug silencioso —
o logo aparece, so que na cor errada.

Solucao: dar namespace por arquivo (.cls-1 -> .par-padrao-1). Tambem tira a
declaracao XML e o id "Camada_2", que colide entre arquivos.
"""
import math
import os
import re

from _caminhos import MARCA, acervo

ORIG = acervo("2026", "Landing Pages", "lp-parcerias-ea", "logos", "LOGOS E SELOS")
DEST = MARCA


MAPA = [
    ("LOGO PADRÃO.svg",         "parceria-padrao",         "padrao"),
    ("LOGO SECUNDÁRIA.svg",     "parceria-secundaria",     "secundaria"),
    ("NEGATIVA.svg",            "parceria-negativa",       "negativa"),
    ("VERSÃO BRANCA.svg",       "parceria-branca",         "branca"),
    ("LOGO OUTLINE.svg",        "parceria-outline",        "outline"),
    ("LOGO OUTLINE BRANCA.svg", "parceria-outline-branca", "outlinebr"),
]

TOKENS = {"#2F24FF": "íris", "#2488FF": "azul coringa", "#2B2E6F": "azul do logotipo",
          "#050634": "navy", "#4F45F5": "violeta", "#772BF2": "roxo"}


def _lin(c):
    return c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4


def lab(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r, g, b = (_lin(int(h[i:i + 2], 16) / 255) for i in (0, 2, 4))
    x = (.4124 * r + .3576 * g + .1805 * b) / .95047
    y = .2126 * r + .7152 * g + .0722 * b
    z = (.0193 * r + .1192 * g + .9505 * b) / 1.08883
    f = lambda t: t ** (1 / 3) if t > .008856 else 7.787 * t + 16 / 116
    fx, fy, fz = f(x), f(y), f(z)
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def de76(a, b):
    la, aa, ba = lab(a); lb, ab, bb = lab(b)
    return math.sqrt((la - lb) ** 2 + (aa - ab) ** 2 + (ba - bb) ** 2)


os.makedirs(DEST, exist_ok=True)
cores_encontradas = set()

print(f"{'arquivo':<26}{'saida':<26}{'classes':>8}{'KB':>7}")
print("-" * 68)
for origem, saida, pref in MAPA:
    p = os.path.join(ORIG, origem)
    if not os.path.exists(p):
        print(f"{origem:<26} AUSENTE"); continue
    t = open(p, encoding="utf-8").read()

    # 1. fora a declaracao XML — invalida dentro de HTML
    t = re.sub(r"<\?xml[^>]*\?>\s*", "", t)
    # 2. ids do Illustrator colidem entre arquivos
    t = re.sub(r'\sid="Camada_[^"]*"', "", t)
    t = re.sub(r'\sdata-name="[^"]*"', "", t)
    # 3. NAMESPACE das classes — o ponto principal
    classes = sorted(set(re.findall(r"cls-(\d+)", t)), key=int)
    for n in classes:
        t = re.sub(rf"\bcls-{n}\b", f"par-{pref}-{n}", t)
    # 4. o SVG precisa escalar no container
    t = re.sub(r"<svg\s", '<svg style="width:100%;height:auto;display:block" ', t, count=1)
    t = re.sub(r"\s+", " ", t).replace("> <", "><").strip()

    for c in re.findall(r"fill: (#[0-9a-fA-F]{3,6})", t):
        cores_encontradas.add(c.upper())

    fp = os.path.join(DEST, saida + ".svg")
    open(fp, "w", encoding="utf-8").write(t)
    print(f"{origem:<26}{saida + '.svg':<26}{len(classes):>8}{round(len(t)/1024,1):>7}")

print("-" * 68)
print("\ncores dos SVGs oficiais, confrontadas com os tokens:")
for c in sorted(cores_encontradas):
    if c in ("#FFF", "#FFFFFF", "#FBFFF7", "#E0E0E0", "#1D1D1B", "#3C3C3B"):
        print(f"   {c:<10} neutro")
        continue
    alvo = min(TOKENS, key=lambda t_: de76(c, t_))
    d = de76(c, alvo)
    v = "é o token" if d < 2 else ("próximo" if d < 10 else "NÃO está nos tokens")
    print(f"   {c:<10} mais próximo: {alvo} ({TOKENS[alvo]})  ΔE≈{d:.1f}  → {v}")
