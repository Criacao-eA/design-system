---
tipo: projeto
papel: inventário-mestre de componentes para o Design System da e-Auditoria
atualizado: 2026-07-20
fonte: extração automática de 6 LPs WordPress + 32 módulos HubSpot (Parcerias, Jornada, Nova News) + eauditoria-brand.skill + guia-replicacao
publico-alvo: equipe de Criação e-Auditoria (donos do banco de elementos)
---

# Design System e-Auditoria — Inventário-mestre de componentes

Este documento consolida TODOS os elementos de UI já existentes e em produção nos materiais
de marketing da e-Auditoria (landing pages WordPress + módulos HubSpot de LP e newsletter).
É a base para transformar o que já existe (mas está fragmentado) em um sistema único,
replicável e escalável — controlado pela equipe de Criação.

**Diagnóstico central:** a e-Auditoria NÃO precisa construir um design system do zero.
Já existe uma biblioteca madura de componentes; o problema é **fragmentação** — os mesmos
componentes e as mesmas cores de marca estão redeclarados com nomes diferentes em cada projeto.
O trabalho do DS é **unificar**, não inventar.

---

## CAMADA 0 — Fundações (tokens)

> Origem: `eauditoria-brand.skill` (canônico) + o que foi observado em produção.
> **A brand skill já define os tokens semânticos.** O débito é que cada LP os reimplementa
> com nomes próprios (ver "Débito crítico" abaixo).

### Cor — núcleo de marca (confirmado em ≥3 arquivos com o mesmo HEX)
| Papel | HEX | Observação |
|---|---|---|
| Navy / ink (fundo escuro, texto forte) | `#050634` | base de todas as seções dark |
| Azul vibrante (coringa) | `#2488ff` | une as verticais |
| Azul-violeta (primária de UI) | `#2f24ff` | cor de botão/link mais usada |
| Violeta | `#4f45f5` | |
| Roxo | `#8439e6` | |
| Ciano (dados em fundo escuro) | `#00ffea` | acento, nunca dominante |
| **Amarelo (CTA)** | `#fec008` | **cor única de CTA** — texto escuro, nunca branco |
| Laranja (energia/ao vivo) | `#fb5507` | |
| Pink (expressivo) | `#ff0071` | |
| Vermelho (alerta/urgência) | `#ff2f34` | com parcimônia |

### Neutras (escala azulada)
`#f5f9fc` (branco gelo) · `#a2b9da` (borda/divisor) · `#576b86` (texto secundário) · `#1e2126` (grafite) · `#000000` (restrito).

### Pastéis (superfícies/fundos — "pastel é palco, cor plena é ator")
Violetas: `#DDD6FE #E8E4FF #F0EBFF #E7DEFF #E7E2FF #EFE6FF` · Azuis: `#C7DBFF #DBE7FF #E4F2FF #EFF3FD` · Pink/lav: `#E5DAFF #FFE1F0 #f8e8ff` · Amarelo: `#fff8e0 #fff0b8 #FFF0C4` · Ciano: `#D9F5F0`.

### Gradientes (biblioteca oficial — usar as receitas, não inventar)
- Texto/palavra em destaque: `135deg #4f45f5→#8439e6` (o mais usado) · tri-tom `125deg #2f24ff→#8439e6→#ff0071` · dados `90deg #00ffea→#4f45f5→#8439e6`.
- Fundo escuro: `140deg #06063a→#0d0540→#1c0860` · `180deg #050634→#0A0C44→#050634`.
- Fundo claro: lavanda `220deg #DDD6FE→#C7DBFF→#E5DAFF` · aurora `135deg #d8e8ff→#f8e8ff→#fff8ee`.
- Masthead newsletter: `122deg #8439E6→#5B4BF2→#2488FF` (fallback sólido `#4F45F5`).
- "AO VIVO": `#FB5507→#FF2F34`.

### Tipografia (100% consistente em TODOS os arquivos — o único token já unificado)
- **Familjen Grotesk** — display/títulos/números (700, tracking negativo, nunca itálico).
- **Manrope** — corpo/CTAs/labels (400–800).
- `@import url('https://fonts.googleapis.com/css2?family=Familjen+Grotesk:wght@400;500;600;700&family=Manrope:wght@400;500;600;700&display=swap');`
- Escala observada: H1 `clamp(40–84px)`, H2 `clamp(28–58px)`, sub 15–19px, âncora/número 46–64px, corpo 14–16px.

### Geometria e efeitos
- Raio: `40px` (seções/painéis), 20–28px (cards), 12–16px (chips/imagens email), `50px`/`100px`/`999px` (pílulas/botões).
- Sombra: família violeta `rgba(47,36,255,X)` / `rgba(60,40,140,.10–.18)`; glow de CTA amarelo `rgba(254,192,8,.36)`.
- Glassmorphism: `rgba(255,255,255,.03–.07)` + `backdrop-filter: blur(12–24px)`.
- Movimento: float 5–6s, twinkle 3s, marquee 34–40s, blob 7–11s, confetti — SEMPRE atrás de `prefers-reduced-motion`.
- **Espaçamento NÃO está tokenizado em lugar nenhum** (valores literais) → tokenizar é tarefa do DS.

### ⚠️ DÉBITO CRÍTICO — fragmentação de tokens (a prioridade nº 1 do DS)
A MESMA cor de marca está redeclarada com 5+ nomes diferentes entre projetos:

| Conceito | MOT | PROC | SPED | SIM | EIRPF | Parcerias |
|---|---|---|---|---|---|---|
| prefixo | `--ea-*` | `--r-*` | `--ea-*` | `--c-*` | `--color-*` | `--c*` |
| navy | `--ea-navy #050634` | `--r-navy #0A1F44` | `#001B30` | `--bg-dark #050634` | `#050634` | `--cdk #06063a` |
| primária | `--ea-blue #8000ff`(⚠roxo!) | `--r-blue #1B4FD8` | `#3563E9` | `--c-violet #4F45F5` | `#2f24ff` | `--cp #2F24FF` |

Além disso: hexadecimais críticos hardcoded fora dos tokens (botão `#FFB124`, cyans `#00D4FF`/`#3AB4F2`),
nomes enganosos (`--ea-blue` = roxo), e o navy oscila entre `#050634` e `#06063a`.
**→ Ação nº 1 do DS: um único arquivo `eauditoria-tokens.css` canônico que todos passam a referenciar.**

---

## CAMADA 1 — Primitivos de UI (~18)

| Primitivo | Variantes reais encontradas | Onde |
|---|---|---|
| **Botão pill primário** | amarelo `#fec008` (LP/evento) · violeta `#2f24ff` (email/institucional) · laranja (PROC) | todos |
| Botão outline / ghost | outline violeta · ghost sobre escuro | vários |
| Botão glow | primário com `box-shadow` glow | Parcerias, Jornada |
| Botão magnético (Luma) | radial glow segue cursor `--x/--y` | MOT, SPED |
| Botão bulletproof (email) | `<td bgcolor radius100>` + `<a>` + `<span !important>` | Nova News |
| **Badge/eyebrow/chip** | badge gradiente · eyebrow uppercase · pill toggle · keyword inline | todos |
| **Status pill / flag** | good/ok/warn · impacto alto/médio/operacional | SIM, Nova News |
| **Card glass** (primitivo universal) | glass-bg + border + blur + barra-topo 3px + hover lift | todos |
| Kicker chip / infocard chip | pílula branca / ícone+texto | Jornada, Parcerias |
| Highlight span (palavra em degradê) | `background-clip:text` em 1–3 palavras | todos |
| Divisor | `<hr>` gradiente · faixa 120px · hairline email `<td height=1>` | vários |
| Contador animado | `[data-count]` rAF, `toLocaleString('pt-BR')` | MOT, SPED, SIM |
| Scroll-reveal | `.reveal→.in` IntersectionObserver + stagger | 5 dos 6 |
| Placeholder listrado | fallback diagonal de imagem | Jornada, LPs |
| Orb/blob/partícula | luz desfocada `blur(80–500px)` · blob orgânico · star-field | MOT, EIRPF, Parcerias |
| Container | 1140–1200px | todos |
| Utilitários responsivos | `.desktop-only/.mobile-only`, `.stack` (email) | todos |
| **Sistema de ícones** ⚠️ | Font Awesome (MOT/PROC/SPED) · SVG inline (SIM) · emoji (EIRPF/Parcerias) — **fragmentado, unificar** | todos |

---

## CAMADA 2 — Blocos web (LP / site WordPress + HubSpot)

### Navegação
- **Header** — 3 variantes: glass-pill flutuante · barra sticky com estado `.scrolled` · absoluto transparente.
- Skip-link (a11y).

### Hero (a dobra mais rica — 8+ variações)
- Split texto + formulário HubSpot (2 col).
- Full-viewport centrado + mockup.
- **3 variantes A/B** (Parcerias): gradiente · minimal (título gigante + photo grid) · centrado.
- **EventHero** (Jornada) — 4 layouts: bento · fotos-no-título · orbitando · dados-ao-redor.

### Prova social
- Faixa de logos de clientes.
- **Stats-band** (3–4 métricas, contadores animados ou estáticos).
- **Depoimentos** — grid estático · carrossel com setas (3/2/1) · depoimento único com vídeo/Instagram.

### Conteúdo
- **Feature-grid / benefícios** (cards ícone+título+texto).
- **Feature-highlights zig-zag** (texto/imagem alternados).
- **MediaText / seção genérica** (50/50, imagem esq/dir, claro/escuro) — o "coringa" reutilizável.
- **Pipeline / steps** (processo numerado; vertical sticky · grid 01-02-03 · comparativo de fluxo).
- **Tripod-timeline** (Passado/Presente/Futuro).
- **Task-carousel** (marquee infinito de tarefas).
- **Comparison-cards** (antes/depois, manual×automático, danger/safe, selo "VS").
- **Panel / impact-box** (card com lista/callout).
- **Result-cards** (Escritório × Cliente).
- **Reasons-grid** ("por que participar", cards pastel inclinados).
- **Takeaways-bento** ("o que você vai levar", bento gradiente).
- **Word-cloud-scatter** (pills que convergem no scroll — interativo).
- **Tabs-feature** (benefícios em abas acessíveis role=tab).
- **Bento-grid** (evento/convidado — data, foto, apresentadora, stat, mini-CTA).
- Repo/manifesto ("de executor para analista").

### Conversão
- **Lead-form** (card branco com embed HubSpot — ID do portal no gerenciador de senhas da equipe).
- **Final-CTA** (banner de fechamento; com glows · star-field + card glass · 3 pilares · badge de escassez).
- **FAQ** (acordeão `<details>` · cards estáticos) — espelha JSON-LD FAQPage.

---

## CAMADA 3 — Dataviz (o diferencial fiscal — sobretudo no Simulador)

kpi-card · dash-kpis (IBS/CBS/economia) · fork (árvore de decisão DAS×Híbrido) · viz browser-card ·
**donut CSS puro** (conic-gradient) · tabela com status pills (NCM/alíquota) · supplier-bars (ranking) ·
status-rows/flags · **tablet/mockup-window** (moldura iPad/browser com iframe) · aliquota-table (antes×depois PIS/COFINS) ·
vis-card (mockup de painel) · floating-card · mini-stat · infographic-box.

---

## CAMADA 4 — Blocos de e-mail (email-safe — newsletter "Radar Tributário")

> Renderização por TABELAS + estilos inline. Mundo técnico separado do web. 640/560/436px.

**Módulos (11):** header/masthead · media-slot · hero · **deadline-anchor** (card navy, número-herói 64px + sweep ciano) ·
**article-list** (lista repetível com pill de impacto colorido) · banner · feature-card · case-study · poll (opção = link rastreável) ·
**event-card** (navy + badge AO VIVO) · footer (compliance + descadastro).

**Primitivos email-safe:** botão bulletproof · pill · divisor hairline · sweep de acento · spacer · imagem fluida · card container · preheader oculto · stack responsivo.

**Sistema de cor de impacto:** alto `#FFE7E7`/`#C7202B` 🔴 · médio `#FFF3D1`/`#9A6A00` 🟡 · operacional `#E2EEFF`/`#1667D6` 🔵.

---

## CAMADA 5 — Padrões de domínio (o insubstituível da e-Auditoria)

### Calculadora-isca (lead magnet fiscal)
- Embed de 3 arquivos escopado por `#ea-calc-<nome>`, gate em 2 etapas (aceite + form HubSpot), `GATE_MODE` teaser/cego (A/B).
- Formatação pt-BR: `R$ 1.234,56`, milhar, `%`, máscara CPF/CNPJ ao digitar.
- Guardrails: nenhum número inventado, sempre disclaimer, ângulo da carteira do contador.

### Evento / webinar (Jornada do Especialista)
- **CountdownBar** (data-target ISO, dias/horas/min/seg, tema sunrise→dusk).
- **AgendaSchedule + TurmaCard dia/tarde** (☀️ warm / 🌙 purple — o motivo mais reutilizado).
- **LiveStream** (embed YouTube vídeo + live-chat, com empty state).
- **SpeakerGrid** (card retrato, badge, bio hover-reveal).
- **JourneyStepper** (jornada gamificada, % de sucesso, confetti, parallax).
- Scarcity-badge (contador de vagas).

---

## REGRAS DE GOVERNANÇA (já documentadas no guia — viram regra do DS)

1. **Sem `&&` no JS do WordPress** (vira `&#038;` e mata o `<script>`) → ternário/if aninhado.
2. **Escopo por wrapper único** (`#ea-calc-x`, `.lc224-`, `.je-lp`) — prefixar todo CSS, nunca seletor global.
3. **Fail-safe sem JS** — conteúdo e números pré-renderizados; JS só adiciona animação.
4. **Captura sempre por embed HubSpot** (portal da e-Auditoria) — nunca form custom, nunca chave de API no front.
5. **Colar em UM bloco HTML Personalizado** (Gutenberg), fonte via `@import` (não `<link>`).
6. **CSS no template, módulos "burros"** (padrão HubSpot: módulo só HubL + fields.json).
7. **Paleta por vertical do produto** (regra 60-20-10; Reforma = 4 cores em equilíbrio).

---

## PLANO DE UNIFICAÇÃO (ordem recomendada)

1. **`eauditoria-tokens.css`** — arquivo único canônico de tokens (resolve a fragmentação nº 1). Namespace único `--ea-*` com nomes semânticos corretos.
2. **Padronizar o sistema de ícones** (escolher 1: SVG inline é o mais portátil/leve).
3. **Catálogo vivo** — página única (Artifact) com preview + código copia-e-cola de cada componente, nas versões web e email.
4. **Normalizar nomenclatura** de componentes (`ea-<categoria>-<nome>`), aposentar classes `.ea-sN` numéricas e prefixos por projeto.
5. Migrar bloco a bloco, validando em 2 peças reais antes de escalar.

---

*Extraído de: lm-motor-do-simples, lm-processamento-inteligente, lm-sped-automatico, Simulador da Reforma, e-IRPF, Parcerias (6 LPs WordPress); módulos HubSpot ea-* de Parcerias, Jornada do Especialista e Nova News (32 módulos); eauditoria-brand.skill e guia-replicacao-embed-wordpress.md.*
