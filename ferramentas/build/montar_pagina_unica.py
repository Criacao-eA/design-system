# -*- coding: utf-8 -*-
"""
Volta ao catalogo de PAGINA UNICA.

A divisao em 9 paginas resolvia o peso, mas quebrava a leitura de sistema: a Criacao
navega o catalogo procurando relacao entre as partes, e isso se perde quando cada
parte mora num endereco. Decisao da lideranca de Criacao: uma pagina so, mesmo pesada.

Reaproveita toda a maquinaria da montagem multipagina (fatiamento de secao, resolucao
de placeholder, regras de grafia) — muda so a composicao final.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import montar_multipagina as mp

DS = mp.DS
SAIDA = os.path.join(DS, "catalogo.html")

# Ordem do documento. Agrupada por leitura, nao por camada tecnica.
ESTRUTURA = [
    ("Marca",             ["marca", "mascotes"]),
    ("Programas",         ["submarcas", "imersao", "aulao", "jogo", "radar",
                           "parcerias", "jornada"]),
    ("Projetos internos", ["premia", "autores"]),
    ("Fundações",         ["cores", "paletas", "paletas-pastel", "gradientes",
                           "tipografia", "geometria", "espacamento",
                           "icones-2d", "icones-3d"]),
    ("Superfícies",       ["padroes", "backgrounds", "vidro"]),
    ("Primitivos",        ["botoes", "badges", "cards", "divisores", "contador",
                           "reveal", "fundos"]),
    ("Blocos web",        ["header", "heros", "urgencia", "video", "logos", "stats",
                           "features", "mediatext", "passos", "comparativo", "abas",
                           "depoimentos", "bento", "faq", "form", "cta", "cta-sticky"]),
    ("Dataviz fiscal",    ["kpis", "donut", "tabela", "virada", "moldura"]),
    ("Evento",            ["countdown", "agenda", "palestrantes", "transmissao"]),
    ("Blocos e-mail",     ["email-masthead", "email-btn", "email-anchor", "email-art",
                           "email-evento", "email-enquete", "email-footer", "email-modelos"]),
    ("Regras",            ["governanca", "pre-voo", "cro"]),
]


def main():
    import json
    bak = open(mp.BAK, encoding="utf-8").read()
    manifest = json.load(open(mp.MANIFEST, encoding="utf-8"))
    svgs = {}
    for n in os.listdir(mp.SVGDIR):
        if n.endswith(".svg"):
            svgs[n[:-4]] = open(os.path.join(mp.SVGDIR, n), encoding="utf-8").read().strip()

    css_base = re.search(r"(?s)<style>(.*?)</style>", bak).group(1)
    script_base = re.search(r"(?s)<script>(.*?)</script>", bak).group(1)

    # catalogo de secoes: BAK + fragmentos
    secoes = mp.fatiar_secoes(bak)
    css_extra = {}
    for arq in mp.FRAGMENTOS:
        p = os.path.join(mp.SCRATCH, arq)
        if not os.path.exists(p):
            print("  AUSENTE:", arq); continue
        frag, css = mp.extrair_css(open(p, encoding="utf-8").read())
        novas = mp.fatiar_secoes(frag)
        secoes.update(novas)
        for sid in novas:
            css_extra[sid] = css_extra.get(sid, "") + "\n" + css
    for arq, alvo in mp.ENXERTOS:
        p = os.path.join(mp.SCRATCH, arq)
        if not os.path.exists(p) or alvo not in secoes:
            continue
        enx, css = mp.extrair_css(open(p, encoding="utf-8").read())
        corte = secoes[alvo].rfind("</section>")
        secoes[alvo] = secoes[alvo][:corte] + "\n" + enx.strip() + "\n    " + secoes[alvo][corte:]
        css_extra[alvo] = css_extra.get(alvo, "") + "\n" + css

    faltas, usadas = [], set()
    corpo, nav, css_pg, ausentes = [], [], [], []
    for titulo, ids in ESTRUTURA:
        presentes = [s for s in ids if s in secoes]
        ausentes += [s for s in ids if s not in secoes]
        if not presentes:
            continue
        nav.append('      <div class="nav-group">%s</div>' % titulo)
        for sid in presentes:
            h = re.search(r"<h2>(.*?)</h2>", secoes[sid])
            nome = re.sub(r"<[^>]+>", "", h.group(1)) if h else sid
            nav.append('      <a href="#%s">%s</a>' % (sid, nome))
            corpo.append(mp.resolver(secoes[sid], manifest, svgs, faltas, usadas))
            if sid in css_extra:
                css_pg.append(css_extra[sid])

    n_sec = sum(len([s for s in ids if s in secoes]) for _, ids in ESTRUTURA)
    abertura = ABERTURA % {"secoes": n_sec}

    doc = MODELO % {
        "css": css_base + "\n" + "\n".join(css_pg),
        "logo": svgs.get("ea-horizontal", ""),
        "nav": "\n".join(nav),
        "abertura": abertura,
        "corpo": "\n\n".join(corpo),
        "script": script_base,
    }
    cont = {"trema": 0, "nowrap": 0}
    doc = mp.aplicar_grafia(doc, cont)
    open(SAIDA, "w", encoding="utf-8").write(doc)

    blocos = doc.count('<div class="comp">')
    print("página única: %d seções | %d blocos | %d imagens | %.2f MB"
          % (n_sec, blocos, len(usadas), len(doc.encode()) / 1024 / 1024))
    print("grafia: %d trema | %d nowrap" % (cont["trema"], cont["nowrap"]))
    if ausentes:
        print("seções não encontradas:", ", ".join(ausentes))
    if faltas:
        print("placeholders não resolvidos:", sorted(set(faltas))[:8])
    orfas = set(manifest) - usadas
    if orfas:
        print("imagens no manifest sem uso: %d (%s)" % (len(orfas), ", ".join(sorted(orfas)[:5])))


ABERTURA = """    <header class="hero">
      <div class="eyebrow">Banco de elementos oficial</div>
      <h1>O sistema visual da <span class="grad ea-brand">e-Auditoria</span>, num lugar só.</h1>
      <p>Marca, sub-marcas, tokens e blocos prontos para landing pages (WordPress + HubSpot)
      e newsletters — com preview ao vivo e código para copiar. Uma fonte única, controlada
      pela Criação, para toda peça sair consistente e escalar sem retrabalho.</p>
      <div class="metrics">
        <div><b>2</b><span>fontes oficiais</span></div>
        <div><b>9</b><span>marcas e programas</span></div>
        <div><b>12</b><span>paletas</span></div>
        <div><b>18</b><span>regras de produção</span></div>
      </div>
    </header>

    <div class="callout">
      <b>Como usar.</b> Cada bloco tem preview e código. Clique em <b>Copiar</b>, cole na peça
      e troque o conteúdo. Onde há vetor, o botão de download gera o PNG na hora, em qualquer
      tamanho. Para web, carregue os tokens (<code>eauditoria-tokens.css</code>) e prefixe tudo
      com o wrapper da peça. Para e-mail, os valores vão inline — o Outlook não entende variáveis.
    </div>

    <div class="callout" style="border-left-color:var(--cyan);background:linear-gradient(135deg,rgba(0,255,234,.09),rgba(47,36,255,.04))">
      <b>Antes de publicar qualquer coisa</b>, passe pelo <a href="#pre-voo">Pré-voo</a>.
      As <a href="#governanca">18 regras de governança</a> não são estilo: cada uma corresponde
      a algo que já quebrou em produção. Esta página é longa de propósito — o catálogo é um
      sistema, e as partes se explicam melhor juntas. Use o menu à esquerda para saltar.
    </div>
"""

MODELO = """<meta charset="utf-8">
<title>Design System e-Auditoria — Catálogo</title>
<meta name="description" content="Catálogo vivo do Design System da e-Auditoria: marca, sub-marcas, mascotes, paletas, superfícies, componentes web, dataviz e e-mail.">

<style>%(css)s</style>

<div class="layout">
  <aside class="side">
    <div class="brand"><a class="brand-logo" href="#topo" aria-label="e-Auditoria — topo do catálogo">%(logo)s</a></div>
    <div class="brand-sub">Design System · v4</div>
    <nav class="nav">
%(nav)s
    </nav>
  </aside>

  <div class="main" id="topo">
    <div class="topbar">
      <span class="crumb">Catálogo de componentes · uso interno da Criação</span>
      <button class="toggle" id="themeBtn">◐ Tema</button>
    </div>

%(abertura)s

%(corpo)s

    <footer>
      Design System <span class="ea-brand">e-Auditoria</span> · v4 — banco de elementos da Criação.
      Arquivos de origem em <code>design-system/assets/</code>.
    </footer>
  </div>
</div>

<script>%(script)s</script>
"""


if __name__ == "__main__":
    main()
