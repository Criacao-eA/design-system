# -*- coding: utf-8 -*-
"""
Montagem MULTIPAGINA do catalogo.

Uma pagina so chegou a 5,7 MB porque cada imagem entra embutida como data URI.
A saida nao e cortar conteudo: e dividir por INTENCAO DE BUSCA. Cada pagina carrega
apenas as suas proprias imagens e apenas o CSS das secoes que hospeda.

O hub mantem a URL que a Criacao ja tem. As paginas filhas linkam de volta para ele.
"""
import json
import os
import re

from _caminhos import DS

SCRATCH = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(DS, "paginas")
BAK = os.path.join(DS, "catalogo-v2.bak.html")
MANIFEST = os.path.join(DS, "assets", "manifest.json")
SVGDIR = os.path.join(DS, "assets", "marca")

HUB_URL = "https://design.e-auditoria.com.br/catalogo.html"

# URLs das paginas filhas, preenchidas apos a publicacao (urls.json).
# Enquanto o arquivo nao existe, os links caem no nome relativo — que e o que
# funciona ao abrir a pasta paginas/ localmente.
_URLS_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "urls.json")
URLS = json.load(open(_URLS_JSON, encoding="utf-8")) if os.path.exists(_URLS_JSON) else {}

# ---------------------------------------------------------------------------
# 1. Mapa de paginas. A ordem das secoes aqui e a ordem no documento.
# ---------------------------------------------------------------------------
PAGINAS = [
    {
        "arquivo": "catalogo.html", "id": "hub",
        "titulo": "Design System e-Auditoria — Catálogo",
        "rotulo": "Início",
        "resumo": "O mapa do sistema e as regras que fazem uma peça sobreviver à publicação.",
        "grupos": [("Produção", ["governanca", "pre-voo", "cro"])],
    },
    {
        "arquivo": "marca.html", "id": "marca",
        "titulo": "Marca — Design System e-Auditoria",
        "rotulo": "Marca",
        "resumo": "A assinatura, o símbolo, as cores da marca e os mascotes.",
        "grupos": [("A marca", ["marca"]), ("Mascotes", ["mascotes"])],
    },
    {
        "arquivo": "imersao.html", "id": "imersao",
        "titulo": "Imersão e-A — Design System e-Auditoria",
        "rotulo": "Imersão e-A",
        "resumo": "O logotipo em pílula com borda em degradê, o sistema de fundo pastel e o padrão de post.",
        "grupos": [("Imersão e-A", ["imersao"])],
    },
    {
        "arquivo": "aulao.html", "id": "aulao",
        "titulo": "Aulão e-A — Design System e-Auditoria",
        "rotulo": "Aulão e-A",
        "resumo": "O motivo de player de mídia: logotipo, controles de transporte, fundos e aplicação social.",
        "grupos": [("Aulão e-A", ["aulao"])],
    },
    {
        "arquivo": "conteudo.html", "id": "conteudo",
        "titulo": "Programas de conteúdo — Design System e-Auditoria",
        "rotulo": "Conteúdo",
        "resumo": "O Jogo da Contabilidade e o Radar Tributário: as duas marcas de conteúdo recorrente.",
        "grupos": [("Programas de conteúdo", ["jogo", "radar"])],
    },
    {
        "arquivo": "marcas.html", "id": "marcas",
        "titulo": "Outras marcas — Design System e-Auditoria",
        "rotulo": "Outras marcas",
        "resumo": "Arena Fiscal, Programa de Parcerias, Jornada do Especialista e os projetos internos.",
        "grupos": [
            ("Sub-marcas", ["submarcas", "parcerias", "jornada"]),
            ("Projetos internos", ["premia", "autores"]),
        ],
    },
    {
        "arquivo": "fundacoes.html", "id": "fundacoes",
        "titulo": "Fundações — Design System e-Auditoria",
        "rotulo": "Fundações",
        "resumo": "Os tokens: cor, paleta por vertical, tipografia, geometria, espaço e ícones.",
        "grupos": [("Cor", ["cores", "paletas", "paletas-pastel", "gradientes"]),
                   ("Forma", ["tipografia", "geometria", "espacamento"]),
                   ("Ícones", ["icones-2d", "icones-3d"])],
    },
    {
        "arquivo": "superficies.html", "id": "superficies",
        "titulo": "Superfícies — Design System e-Auditoria",
        "rotulo": "Superfícies",
        "resumo": "O que preenche o fundo: padrões tileáveis, backgrounds e o sistema de vidro.",
        "grupos": [("Superfícies", ["padroes", "backgrounds", "vidro"])],
    },
    {
        "arquivo": "componentes.html", "id": "componentes",
        "titulo": "Componentes — Design System e-Auditoria",
        "rotulo": "Componentes",
        "resumo": "Os blocos que montam uma peça: primitivos, dobras de LP, dataviz, evento e e-mail.",
        "grupos": [
            ("Primitivos", ["botoes", "badges", "cards", "divisores", "contador", "reveal", "fundos"]),
            ("Blocos web", ["header", "heros", "urgencia", "video", "logos", "stats", "features",
                            "mediatext", "passos", "comparativo", "abas", "depoimentos", "bento",
                            "faq", "form", "cta", "cta-sticky"]),
            ("Dataviz fiscal", ["kpis", "donut", "tabela", "virada", "moldura"]),
            ("Evento", ["countdown", "agenda", "palestrantes", "transmissao"]),
            ("E-mail", ["email-masthead", "email-btn", "email-anchor", "email-art",
                        "email-evento", "email-enquete", "email-footer"]),
        ],
    },
]

# fragmentos externos: arquivo -> lista de ids de secao que ele contem
FRAGMENTOS = [
    "sec-marca.html", "sec-submarcas.html", "sec-mascotes.html", "sec-imersao.html",
    "sec-aulao.html", "sec-jogo.html", "sec-radar.html", "sec-parcerias-jornada.html",
    "sec-premia-autores.html", "sec-paletas.html", "sec-paletas-pastel.html",
    "sec-email-modelos.html", "sec-icones.html", "sec-padroes.html", "sec-backgrounds.html", "sec-vidro.html",
]
ENXERTOS = [("sec-vidro-refino.html", "vidro")]

PROTEGIDO = re.compile(r"(?is)<(pre|svg|style|script)\b.*?</\1>")
TERMOS_NB = ["Reforma Tributária", "Simples Nacional", "Simples Híbrido",
             "Lucro Presumido", "Lucro Real"]


# ---------------------------------------------------------------------------
def extrair_css(frag):
    css = []
    frag = re.sub(r"<!--CSS-INICIO-->(.*?)<!--CSS-FIM-->",
                  lambda m: css.append(m.group(1)) or "", frag, flags=re.S)
    return frag.strip(), "\n".join(css)


def fatiar_secoes(html):
    """Devolve {id: html_da_secao} preservando a ordem de aparicao."""
    out = {}
    for m in re.finditer(r'<section id="([a-z0-9\-]+)"', html):
        sid = m.group(1)
        ini = m.start()
        prof, i = 0, ini
        while i < len(html):
            if html.startswith("<section", i):
                prof += 1
            elif html.startswith("</section>", i):
                prof -= 1
                if prof == 0:
                    out[sid] = html[ini:i + 10]
                    break
            i += 1
    return out


def resolver(txt, manifest, svgs, faltas, usadas):
    def _img(m):
        k = m.group(1)
        if k in manifest:
            usadas.add(k)
            return manifest[k]
        faltas.append(("IMG", k))
        return ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='320' "
                "height='180'%3E%3Crect width='320' height='180' fill='%23e2e7f3'/%3E%3C/svg%3E")

    def _svg(m):
        k = m.group(1)
        if k in svgs:
            return svgs[k]
        faltas.append(("SVG", k))
        return "<!-- svg ausente: %s -->" % k

    txt = re.sub(r"\{\{IMG:([a-z0-9\-]+)\}\}", _img, txt)
    txt = re.sub(r"\{\{SVG:([a-z0-9\-]+)\}\}", _svg, txt)
    return txt


def aplicar_grafia(doc, cont):
    # O trema e trocado no documento INTEIRO, inclusive dentro de <pre>: ali ele
    # aparece em comentario e rotulo de exemplo, nunca como sintaxe. Ja o nowrap
    # injeta HTML, entao esse continua so fora das regioes protegidas.
    n = doc.count("ë-A")
    if n:
        cont["trema"] += n
        doc = doc.replace("ë-AUDITORIA", "e-AUDITORIA").replace("ë-A", "e-A")

    partes, ultimo = [], 0
    for m in PROTEGIDO.finditer(doc):
        partes.append(("livre", doc[ultimo:m.start()]))
        partes.append(("prot", m.group(0)))
        ultimo = m.end()
    partes.append(("livre", doc[ultimo:]))
    saida = []
    for tipo, tr in partes:
        if tipo == "prot":
            saida.append(tr); continue

        def _t(mm):
            s = mm.group(1)
            n = s.count("ë-A")
            if n:
                cont["trema"] += n
                s = s.replace("ë-AUDITORIA", "e-AUDITORIA").replace("ë-A", "e-A")
            for termo in TERMOS_NB:
                if termo in s:
                    cont["nowrap"] += s.count(termo)
                    s = s.replace(termo, "\x00" + termo + "\x01")
            return ">" + s + "<"

        tr = re.sub(r">([^<>]+)<", _t, tr)

        # o trema tambem precisa sair de alt= e aria-label=, que sao texto lido
        # em voz alta por leitor de tela — nao da para tratar so no no de texto
        def _attr(mm):
            v = mm.group(2)
            if "ë-A" in v:
                cont["trema"] += v.count("ë-A")
                v = v.replace("ë-AUDITORIA", "e-AUDITORIA").replace("ë-A", "e-A")
            return '%s="%s"' % (mm.group(1), v)

        tr = re.sub(r'\b(alt|aria-label|title)="([^"]*)"', _attr, tr)
        saida.append(tr)
    doc = "".join(saida)
    return doc.replace("\x00", '<span class="ea-nb">').replace("\x01", "</span>")


# ---------------------------------------------------------------------------
def main():
    os.makedirs(SAIDA, exist_ok=True)
    bak = open(BAK, encoding="utf-8").read()
    manifest = json.load(open(MANIFEST, encoding="utf-8"))
    svgs = {}
    for n in os.listdir(SVGDIR):
        if n.endswith(".svg"):
            svgs[n[:-4]] = open(os.path.join(SVGDIR, n), encoding="utf-8").read().strip()

    # --- chrome comum ---
    css_base = re.search(r"(?s)<style>(.*?)</style>", bak).group(1)
    script_base = re.search(r"(?s)<script>(.*?)</script>", bak).group(1)
    logo_topo = svgs.get("ea-horizontal", "")

    # --- catalogo de secoes: as do BAK + as dos fragmentos ---
    secoes = fatiar_secoes(bak)
    css_extra = {}          # id_secao -> css
    for arq in FRAGMENTOS:
        p = os.path.join(SCRATCH, arq)
        if not os.path.exists(p):
            print("  AUSENTE:", arq); continue
        frag, css = extrair_css(open(p, encoding="utf-8").read())
        novas = fatiar_secoes(frag)
        secoes.update(novas)
        for sid in novas:
            css_extra[sid] = css_extra.get(sid, "") + "\n" + css

    for arq, alvo in ENXERTOS:
        p = os.path.join(SCRATCH, arq)
        if not os.path.exists(p) or alvo not in secoes:
            continue
        enx, css = extrair_css(open(p, encoding="utf-8").read())
        corte = secoes[alvo].rfind("</section>")
        secoes[alvo] = secoes[alvo][:corte] + "\n" + enx.strip() + "\n    " + secoes[alvo][corte:]
        css_extra[alvo] = css_extra.get(alvo, "") + "\n" + css

    # --- monta cada pagina ---
    faltas, relatorio = [], []
    todas_usadas = set()
    for pg in PAGINAS:
        ids = [s for _, lst in pg["grupos"] for s in lst]
        faltando = [s for s in ids if s not in secoes]
        corpo, css_pg, usadas = [], [], set()
        for sid in ids:
            if sid not in secoes:
                continue
            corpo.append(resolver(secoes[sid], manifest, svgs, faltas, usadas))
            if sid in css_extra:
                css_pg.append(css_extra[sid])
        todas_usadas |= usadas

        # Navegacao. Modelo hub-and-spoke: o hub lista todas as paginas; as filhas
        # so voltam para ele. Assim nenhuma pagina precisa saber a URL das irmas —
        # o que permite publicar cada uma UMA vez, sem passe de correcao de links.
        nav = []
        if pg["id"] == "hub":
            nav.append('      <div class="nav-group">Catálogo</div>')
            for outra in PAGINAS[1:]:
                nav.append('      <a href="%s">%s</a>' % (URLS.get(outra["id"], outra["arquivo"]),
                                                          outra["rotulo"]))
        else:
            nav.append('      <div class="nav-group">Catálogo</div>')
            nav.append('      <a href="%s">◂ Índice do catálogo</a>' % HUB_URL)
        for titulo, lst in pg["grupos"]:
            presentes = [s for s in lst if s in secoes]
            if not presentes:
                continue
            nav.append('      <div class="nav-group">%s</div>' % titulo)
            for sid in presentes:
                h = re.search(r"<h2>(.*?)</h2>", secoes[sid])
                nome = re.sub(r"<[^>]+>", "", h.group(1)) if h else sid
                nav.append('      <a href="#%s">%s</a>' % (sid, nome))

        if pg["id"] == "hub":
            cartoes = []
            for i, outra in enumerate(PAGINAS[1:], start=1):
                n_sec = sum(len([s for s in lst if s in secoes]) for _, lst in outra["grupos"])
                cartoes.append(
                    '        <a href="%s">\n'
                    '          <span class="n">%02d · %d seções</span>\n'
                    '          <h3>%s</h3>\n'
                    '          <p>%s</p>\n'
                    '        </a>' % (URLS.get(outra["id"], outra["arquivo"]), i, n_sec,
                                      outra["rotulo"], outra["resumo"]))
            corpo.insert(0, HUB_ABERTURA % {"mapa": "\n".join(cartoes)})

        doc = PAGINA_MODELO % {
            "titulo": pg["titulo"],
            "resumo": pg["resumo"],
            "css": css_base + "\n" + "\n".join(css_pg) + CSS_MULTI,
            "logo": logo_topo,
            "hub": HUB_URL,
            "nav": "\n".join(nav),
            "rotulo": pg["rotulo"],
            "corpo": "\n\n".join(corpo) if corpo else HUB_CORPO,
            "script": script_base,
        }
        cont = {"trema": 0, "nowrap": 0}
        doc = aplicar_grafia(doc, cont)

        # ancora que aponta para secao que NAO esta nesta pagina viraria link morto.
        # Manda para o indice: a pessoa escolhe de la. Melhor um desvio que um 404.
        presentes = set(re.findall(r'<section id="([a-z0-9\-]+)"', doc)) | {"topo"}
        cruzados = []

        def _ancora(mm):
            alvo = mm.group(2)
            if alvo in presentes:
                return mm.group(0)
            cruzados.append(alvo)
            return '%shref="%s"' % (mm.group(1), HUB_URL)

        # SO em <a href="#...">. Um href="#id" dentro de SVG e referencia interna
        # (<use>, filtro, gradiente) — reescrever aquilo quebra o desenho.
        doc = re.sub(r'(<a\s[^>]*?)href="#([a-zA-Z0-9\-_]+)"', _ancora, doc)
        if cruzados:
            print("  %s: %d âncora(s) de outra página redirecionada(s) ao índice (%s)"
                  % (pg["arquivo"], len(cruzados), ", ".join(sorted(set(cruzados)))))
        destino = os.path.join(SAIDA, pg["arquivo"])
        open(destino, "w", encoding="utf-8").write(doc)
        relatorio.append((pg["arquivo"], len(ids) - len(faltando), len(usadas),
                          len(doc.encode()) / 1024 / 1024, faltando))

    print(f"{'pagina':<20}{'seções':>8}{'imgs':>6}{'MB':>7}   faltando")
    print("-" * 62)
    for a, n, i, mb, f in relatorio:
        print(f"{a:<20}{n:>8}{i:>6}{mb:>7.2f}   {','.join(f) if f else '-'}")
    print("-" * 62)
    print(f"total {sum(r[3] for r in relatorio):.2f} MB distribuídos (era 5,72 MB numa página)")
    orfas = set(manifest) - todas_usadas
    if orfas:
        print(f"imagens no manifest sem uso: {len(orfas)}")
    if faltas:
        print("placeholders não resolvidos:", sorted(set(faltas))[:10])


CSS_MULTI = """
  .nav a.atual{background:var(--panel-2);color:var(--ink);font-weight:700;
    box-shadow:inset 2px 0 0 var(--primary)}
  .pagina-tag{font-size:11px;text-transform:uppercase;letter-spacing:.12em;
    color:var(--primary);font-weight:700;margin-bottom:10px}
  .mapa{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px;margin:26px 0}
  .mapa a{display:block;background:var(--panel);border:1px solid var(--line);
    border-radius:var(--r-lg);padding:22px;transition:.18s var(--ease);color:var(--ink)}
  .mapa a:hover{border-color:var(--primary);transform:translateY(-2px);box-shadow:var(--shadow)}
  .mapa h3{font-size:1.1rem;margin:0 0 6px}
  .mapa p{margin:0;font-size:13px;color:var(--ink-soft)}
  .mapa .n{font-family:var(--font-mono);font-size:11px;color:var(--primary);display:block;margin-bottom:8px}
"""

PAGINA_MODELO = """<meta charset="utf-8">
<title>%(titulo)s</title>
<meta name="description" content="%(resumo)s">

<style>%(css)s</style>

<div class="layout">
  <aside class="side">
    <div class="brand"><a class="brand-logo" href="%(hub)s" aria-label="e-Auditoria — início do catálogo">%(logo)s</a></div>
    <div class="brand-sub">Design System · v4</div>
    <nav class="nav">
%(nav)s
    </nav>
  </aside>

  <div class="main" id="topo">
    <div class="topbar">
      <span class="crumb">%(rotulo)s · uso interno da Criação</span>
      <button class="toggle" id="themeBtn">◐ Tema</button>
    </div>

%(corpo)s

    <footer>
      Design System <span class="ea-brand">e-Auditoria</span> · v4 — banco de elementos da Criação.
      Arquivos de origem em <code>design-system/assets/</code>.
    </footer>
  </div>
</div>

<script>%(script)s</script>
"""

HUB_CORPO = "<p>—</p>"

HUB_ABERTURA = """    <header class="hero">
      <div class="eyebrow">Banco de elementos oficial</div>
      <h1>O sistema visual da <span class="grad ea-brand">e-Auditoria</span>, num lugar só.</h1>
      <p>Tokens, marca, sub-marcas e blocos prontos para landing pages (WordPress + HubSpot) e
      newsletters — com preview ao vivo e código para copiar. Uma fonte única, controlada pela
      Criação, para toda peça sair consistente e escalar sem retrabalho.</p>
      <div class="metrics">
        <div><b>2</b><span>fontes oficiais</span></div>
        <div><b>9</b><span>marcas e programas</span></div>
        <div><b>12</b><span>paletas</span></div>
        <div><b>18</b><span>regras de produção</span></div>
      </div>
    </header>

    <div class="callout">
      <b>Como o catálogo está organizado.</b> Ele foi dividido em páginas por
      <b>intenção de busca</b>, não por camada técnica — e cada página carrega só os próprios
      arquivos, para abrir rápido. Comece pelo cartão que descreve o que você precisa.
      As regras de publicação ficam aqui no início, porque valem para tudo.
    </div>

    <div class="mapa">
%(mapa)s
    </div>

    <div class="callout" style="border-left-color:var(--cyan);background:linear-gradient(135deg,rgba(0,255,234,.09),rgba(47,36,255,.04))">
      <b>Antes de publicar qualquer coisa</b>, passe pelo <a href="#pre-voo">Pré-voo</a>. As
      regras de <a href="#governanca">Governança</a> não são estilo: cada uma corresponde a
      algo que já quebrou em produção.
    </div>
"""


if __name__ == "__main__":
    main()
