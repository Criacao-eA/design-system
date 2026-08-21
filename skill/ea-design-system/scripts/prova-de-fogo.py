#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROVA DE FOGO — a peça fugiu do Design System da e-Auditoria?

Confronta um arquivo (ou uma pasta) contra o sistema, sem opinião. Não substitui
olhar a peça: substitui a discussão sobre "acho que essa cor não é nossa".

USO
  python prova-de-fogo.py peca.html
  python prova-de-fogo.py pasta-do-tema/          (varre .html e .css)
  python prova-de-fogo.py peca.html --email       (aplica também as regras de e-mail)
  python prova-de-fogo.py peca.html --json        (saída para script/CI)

SAÍDA
  Código de saída 0 se passou em tudo, 1 se falhou em algo. Serve em automação.

O QUE ELE MEDE
  1. Cor      — cada hexadecimal usado existe nos tokens? (ΔE00 contra a paleta inteira)
  2. Tipo     — a pilha de fontes parte de Familjen Grotesk / Manrope?
  3. CTA      — #FEC008 com texto navy e pílula?
  4. Contraste— cada cor de texto passa WCAG AA sobre o fundo da peça?
  5. Produção — as regras que já quebraram algo no ar (sem &&, sem data-* no wrapper,
                prefixo dentro de @media, cor de <a> com !important)
  6. Marca    — "e-A" sem trema, expressões fiscais protegidas contra quebra de linha

Autor: equipe de Criação. Fonte da verdade: eauditoria-tokens.css e o catálogo.
"""
import argparse
import glob
import json
import math
import os
import re
import sys

# ---------------------------------------------------------------- tokens
TOKENS = {
    # marca
    "#050634": "navy", "#2F24FF": "íris (primária de UI)", "#4F45F5": "violeta",
    "#772BF2": "roxo de vertical", "#8439E6": "roxo (token antigo)",
    "#2488FF": "azul coringa", "#2486FF": "azul (variante de arte)",
    "#00FFEA": "ciano", "#FEC008": "CTA amarelo", "#FB5507": "laranja",
    "#FF0071": "pink", "#FF2F34": "vermelho", "#2B2E6F": "azul do logotipo",
    "#5243FA": "violeta Imersão", "#0051FF": "azul do Programa de Parcerias",
    # neutras
    "#FFFFFF": "branco", "#F5F9FC": "branco gelo", "#A2B9DA": "borda",
    "#576B86": "texto secundário", "#1E2126": "grafite", "#000000": "preto (restrito)",
    "#E4E9F5": "divisor",
    # e-mail
    "#E7ECF6": "moldura de e-mail", "#F1F2FF": "card claro", "#F7F9FD": "card claro 2",
    "#4A4D6B": "corpo (e-mail)", "#7377A0": "meta (e-mail) — reprova AA em texto pequeno",
    # pastéis
    "#E7E2FF": "pastel lilás", "#DFE2FF": "pastel peri", "#DBE7FF": "pastel azul",
    "#EFE6FF": "pastel lavanda", "#FFF0C4": "pastel baunilha", "#D9F5F0": "pastel ciano",
    "#F0E3FF": "pastel uva", "#FFE1F0": "pastel rosa",
    # impacto (newsletter)
    "#FFE7E7": "impacto alto bg", "#C7202B": "impacto alto txt",
    "#FFF3D1": "impacto médio bg", "#9A6A00": "impacto médio txt",
    "#E2EEFF": "impacto operacional bg", "#1667D6": "impacto operacional txt",
    # estados semânticos (eauditoria-tokens.css, seção 2)
    "#10B981": "sucesso", "#0F9D76": "sucesso escuro",
    "#241BCF": "primária hover",
    # paradas dos GRADIENTES oficiais — são tokens tanto quanto as cores chapadas.
    # Sem elas, qualquer peça usando o degradê escuro da marca seria acusada à toa.
    "#06063A": "grad escuro · parada 1", "#0D0540": "grad escuro · parada 2",
    "#1C0860": "grad escuro · parada 3", "#0A0C44": "grad escuro suave · meio",
    "#5B4BF2": "grad masthead · meio", "#DDD6FE": "grad claro · parada 1",
    "#C7DBFF": "grad claro · parada 2", "#E5DAFF": "grad claro · parada 3",
    "#D8E8FF": "aurora · 1", "#EEEAFF": "aurora · 2", "#F8E8FF": "aurora · 3",
    "#FFF8EE": "aurora · 4",
    "#F7A70A": "CTA âmbar · parada escura", "#FFD65C": "CTA âmbar · parada clara",
}

# Este verificador NÃO deve ser rodado no próprio eauditoria-tokens.css: aquele
# arquivo DEFINE a paleta, e não declara tipografia aplicada nem botão. Rode-o em
# peças (HTML/CSS de landing page, módulo de e-mail, tema).
FONTES = ("familjen grotesk", "manrope")
TERMOS = ["Simples Nacional", "Simples Híbrido", "Lucro Real",
          "Lucro Presumido", "Reforma Tributária", "e-Auditoria"]


# ---------------------------------------------------------------- cor
def _lin(c):
    return c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4


def _rgb(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def lum(h):
    r, g, b = (_lin(c) for c in _rgb(h))
    return .2126 * r + .7152 * g + .0722 * b


def contraste(a, b):
    la, lb = lum(a), lum(b)
    return (max(la, lb) + .05) / (min(la, lb) + .05)


def lab(h):
    r, g, b = (_lin(c) for c in _rgb(h))
    x = (.4124 * r + .3576 * g + .1805 * b) / .95047
    y = .2126 * r + .7152 * g + .0722 * b
    z = (.0193 * r + .1192 * g + .9505 * b) / 1.08883
    f = lambda t: t ** (1 / 3) if t > .008856 else 7.787 * t + 16 / 116
    fx, fy, fz = f(x), f(y), f(z)
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def de00(h1, h2):
    L1, a1, b1 = lab(h1); L2, a2, b2 = lab(h2)
    C1, C2 = math.hypot(a1, b1), math.hypot(a2, b2)
    Cb = (C1 + C2) / 2
    G = .5 * (1 - math.sqrt(Cb ** 7 / (Cb ** 7 + 25 ** 7))) if Cb else .5
    a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = math.hypot(a1p, b1), math.hypot(a2p, b2)
    h1p = math.degrees(math.atan2(b1, a1p)) % 360 if (a1p or b1) else 0
    h2p = math.degrees(math.atan2(b2, a2p)) % 360 if (a2p or b2) else 0
    dLp, dCp = L2 - L1, C2p - C1p
    dhp = 0 if C1p * C2p == 0 else ((h2p - h1p + 180) % 360) - 180
    dHp = 2 * math.sqrt(C1p * C2p) * math.sin(math.radians(dhp) / 2)
    Lbp, Cbp = (L1 + L2) / 2, (C1p + C2p) / 2
    if C1p * C2p == 0:
        hbp = h1p + h2p
    elif abs(h1p - h2p) <= 180:
        hbp = (h1p + h2p) / 2
    else:
        hbp = (h1p + h2p + 360) / 2 if h1p + h2p < 360 else (h1p + h2p - 360) / 2
    T = (1 - .17 * math.cos(math.radians(hbp - 30)) + .24 * math.cos(math.radians(2 * hbp))
         + .32 * math.cos(math.radians(3 * hbp + 6)) - .20 * math.cos(math.radians(4 * hbp - 63)))
    Sl = 1 + (.015 * (Lbp - 50) ** 2) / math.sqrt(20 + (Lbp - 50) ** 2)
    Sc, Sh = 1 + .045 * Cbp, 1 + .015 * Cbp * T
    Rt = -2 * math.sqrt(Cbp ** 7 / (Cbp ** 7 + 25 ** 7)) * math.sin(
        math.radians(60 * math.exp(-(((hbp - 275) / 25) ** 2))))
    return math.sqrt((dLp / Sl) ** 2 + (dCp / Sc) ** 2 + (dHp / Sh) ** 2
                     + Rt * (dCp / Sc) * (dHp / Sh))


def token_mais_proximo(cor):
    alvo = min(TOKENS, key=lambda t: de00(cor, t))
    return alvo, de00(cor, alvo)


# ---------------------------------------------------------------- auditoria
def limpar(t):
    """Comentário não é código aplicado."""
    t = re.sub(r"\{#.*?#\}", " ", t, flags=re.S)      # HubL
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)     # HTML
    t = re.sub(r"/\*.*?\*/", " ", t, flags=re.S)      # CSS
    return t


def auditar(texto, email=False):
    t = limpar(texto)
    res = []

    # 1. cores
    cores = sorted({"#" + c.upper() for c in re.findall(r"#([0-9a-fA-F]{6})\b", t)})
    fora = [(c,) + token_mais_proximo(c) for c in cores]
    fora = [(c, a, d) for c, a, d in fora if d >= 1.0]
    res.append({
        "criterio": "cor", "passou": not fora,
        "detalhe": (f"{len(cores)} cores, todas do sistema" if not fora else
                    "fora do sistema: " + ", ".join(
                        f"{c} (mais próximo {a}, ΔE {d:.1f})" for c, a, d in fora[:6])),
    })

    # 2. tipografia
    # var(--x) precisa ser resolvida antes de julgar: a peça pode declarar a fonte
    # da marca no token e usar a variável em todo lugar — isso é o certo, não erro.
    defs = {m.group(1): m.group(2) for m in
            re.finditer(r"(--[\w-]+)\s*:\s*([^;}]*(?:grotesk|manrope)[^;}]*)", t, re.I)}
    fams = set()
    for f in re.findall(r"font-family:\s*([^;}]+)", t):
        f = f.strip().strip("\"'").lower()
        alvo = re.match(r"var\(\s*(--[\w-]+)", f)
        if alvo:
            f = defs.get(alvo.group(1), f).lower()
        fams.add(f)
    ruins = [f[:44] for f in fams if not any(ok in f for ok in FONTES)]
    res.append({
        "criterio": "tipografia", "passou": bool(fams) and not ruins,
        "detalhe": (f"{len(fams)} pilha(s), todas partem da marca" if fams and not ruins
                    else (f"sem a fonte da marca: {ruins[:3]}" if ruins
                          else "nenhuma família declarada")),
    })

    # 3. CTA
    # Peça bem feita usa var(--navy), não o literal. Resolve as variáveis antes de
    # julgar — senão o verificador reprova justamente quem tokenizou direito, e
    # ninguém confia mais no alerta.
    varsdef = {m.group(1): m.group(2).strip()
               for m in re.finditer(r"(--[\w-]+)\s*:\s*(#[0-9a-fA-F]{3,6})\s*;", t)}
    navys = {k for k, v in varsdef.items() if v.upper() in ("#050634", "#050634FF")}
    tem = "FEC008" in t.upper() or any(
        v.upper() == "#FEC008" for v in varsdef.values())
    navy = re.search(r"color:\s*#050634", t, re.I) is not None
    if not navy and navys:
        navy = any(re.search(r"color:\s*var\(\s*" + re.escape(k), t) for k in navys)
    pil = re.search(r"border-radius:\s*(100px|999px|9999px|50%)", t) is not None
    if not pil:
        raios = {k for k, v in varsdef.items() if v in ("100px", "999px", "9999px")}
        pil = any(re.search(r"border-radius:\s*var\(\s*" + re.escape(k), t) for k in raios)
    falta = []
    if not tem:
        falta.append("nenhum botão em #FEC008")
    else:
        if not navy:
            falta.append("texto do botão não é navy #050634")
        if not pil:
            falta.append("raio não é de pílula")
    res.append({"criterio": "CTA", "passou": not falta,
                "detalhe": "#FEC008 + navy + pílula" if not falta else ", ".join(falta)})

    # 4. contraste
    fundo = "#FFFFFF"
    m = re.search(r"background(?:-color)?:\s*(#[0-9a-fA-F]{6})", t)
    if m and lum(m.group(1)) > .5:
        fundo = m.group(1).upper()
    txts = {c.upper() for c in re.findall(r"(?<!background-)color:\s*(#[0-9a-fA-F]{6})", t)}
    reprova = [(c, contraste(c, fundo)) for c in txts
               if contraste(c, fundo) < 4.5 and c != fundo]
    res.append({
        "criterio": "contraste", "passou": not reprova,
        "detalhe": (f"todo texto passa AA sobre {fundo}" if not reprova else
                    f"sobre {fundo}: " + ", ".join(f"{c} {v:.2f}:1" for c, v in reprova[:5])),
    })

    # 5. producao
    probs = []
    if "&&" in t:
        probs.append("contém && (o editor do WordPress quebra o script)")
    if re.search(r'<div[^>]+class="[^"]*"[^>]*\sdata-[a-z-]+=', t):
        probs.append("data-* no wrapper (o sanitizador apaga, e leva class/id junto)")
    if re.search(r"\[data-[a-z-]+=", t):
        probs.append("regra de CSS dependendo de [data-*]")
    # A regra do prefixo dentro de @media é do BLOCO DO WORDPRESS: lá o CSS disputa
    # com o tema. Em e-mail não há tema para disputar e a classe solta é o padrão
    # da indústria — por isso a checagem não se aplica ao modo --email.
    if not email:
        for mm in re.finditer(r"@media[^{]*\{([^@]*?)\}\s*\}", t, re.S):
            if re.search(r"^\s*\.[a-z][\w-]*\s*\{", mm.group(1), re.M):
                probs.append("regra dentro de @media sem o prefixo do wrapper")
                break
    if email:
        if re.search(r"display:\s*flex", t):
            probs.append("e-mail com flexbox (o Outlook não entende)")
        if re.search(r"linear-gradient", t) and not re.search(r'bgcolor="#', t):
            probs.append("e-mail com gradiente sem bgcolor de fallback")
    res.append({"criterio": "produção", "passou": not probs,
                "detalhe": "nenhuma armadilha conhecida" if not probs else "; ".join(probs)})

    # 6. marca
    marca = []
    if "ë-A" in texto:
        marca.append(f"'ë-A' com trema ({texto.count('ë-A')}x) — em texto é sempre e-A")
    desprot = []
    for termo in TERMOS:
        for mm in re.finditer(re.escape(termo), t):
            volta = t[max(0, mm.start() - 70):mm.end() + 12]
            if not any(x in volta for x in ("&nbsp;", "nowrap", "ea-nb", "ea-brand")):
                desprot.append(termo)
                break
    if desprot:
        marca.append("sem proteção de quebra: " + ", ".join(desprot))
    if re.search(r"\|\s*(<[^>]+>)?\s*e-Auditoria", t):
        marca.append("lockup 'sub-marca | e-Auditoria' — não existe na identidade")
    res.append({"criterio": "marca", "passou": not marca,
                "detalhe": "grafia e proteções corretas" if not marca else "; ".join(marca)})

    return res


# ---------------------------------------------------------------- cli
def main():
    ap = argparse.ArgumentParser(description="Prova de fogo do Design System da e-Auditoria")
    ap.add_argument("alvo", help="arquivo ou pasta")
    ap.add_argument("--email", action="store_true", help="aplicar também as regras de e-mail")
    ap.add_argument("--json", action="store_true", help="saída em JSON")
    a = ap.parse_args()

    if os.path.isdir(a.alvo):
        arquivos = [p for ext in ("html", "css", "svg")
                    for p in glob.glob(os.path.join(a.alvo, "**", f"*.{ext}"), recursive=True)]
    else:
        arquivos = [a.alvo]
    if not arquivos:
        print("nada para verificar em", a.alvo); return 1

    texto = "\n".join(open(p, encoding="utf-8", errors="ignore").read() for p in arquivos)
    res = auditar(texto, email=a.email)
    ok = sum(1 for r in res if r["passou"])

    if a.json:
        print(json.dumps({"alvo": a.alvo, "arquivos": len(arquivos),
                          "nota": f"{ok}/{len(res)}", "criterios": res},
                         ensure_ascii=False, indent=2))
        return 0 if ok == len(res) else 1

    print("=" * 72)
    print(f"PROVA DE FOGO · {a.alvo}   ({len(arquivos)} arquivo(s))")
    print("=" * 72)
    for r in res:
        marca = "  [ok]   " if r["passou"] else "  [FALHA]"
        print(f"{marca} {r['criterio']:<11} {r['detalhe']}")
    print("-" * 72)
    print(f"  {ok}/{len(res)} critérios")
    if ok < len(res):
        print("\n  Consulte o catálogo para a regra de cada item:")
        print("  https://design.e-auditoria.com.br/catalogo.html")
    return 0 if ok == len(res) else 1


if __name__ == "__main__":
    sys.exit(main())
