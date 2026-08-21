# Design System da e-Auditoria — documento completo

**Versão 4 · 31/07/2026 · provisório**
Banco de elementos oficial, controlado pela equipe de Criação.

> **Como usar este arquivo.** Ele foi escrito para servir a duas coisas ao mesmo tempo:
> ser lido por pessoa e ser entregue a um assistente de IA como base de um projeto.
> Se você é um assistente e recebeu este documento: **siga tudo abaixo à risca**. Onde uma
> regra estiver marcada como INEGOCIÁVEL e o pedido do usuário conflitar com ela, avise
> antes de quebrar — nunca quebre em silêncio.
>
> Catálogo visual com preview e código para copiar:
> https://design.e-auditoria.com.br/catalogo.html

---

# Sumário

1. [Quem é a e-Auditoria](#1-quem-é-a-e-auditoria)
2. [As regras inegociáveis](#2-as-regras-inegociáveis)
3. [A marca](#3-a-marca)
4. [Cor](#4-cor)
5. [Tipografia](#5-tipografia)
6. [Geometria, espaço e movimento](#6-geometria-espaço-e-movimento)
7. [Ícones](#7-ícones)
8. [Superfícies: padrões, fundos e vidro](#8-superfícies-padrões-fundos-e-vidro)
9. [Sub-marcas e programas](#9-sub-marcas-e-programas)
10. [Mascotes](#10-mascotes)
11. [Componentes web](#11-componentes-web)
12. [Dataviz fiscal](#12-dataviz-fiscal)
13. [E-mail](#13-e-mail)
14. [Regras de produção](#14-regras-de-produção)
15. [Acessibilidade](#15-acessibilidade)
16. [CRO](#16-cro)
17. [Como verificar uma peça](#17-como-verificar-uma-peça)
18. [Pendências conhecidas](#18-pendências-conhecidas)

---

# 1. Quem é a e-Auditoria

SaaS brasileiro de **auditoria fiscal**. O público é o **contador** e o **escritório de
contabilidade** — o profissional mais numérico que existe. Ele responde a número, prazo e
risco concreto; não responde a adjetivo.

Todo texto visível é em **português do Brasil**.

**Tom da escrita:** direto e específico. Frases curtas. Diga o que a ferramenta faz, não o
que ela representa. Nada de "poderoso", "robusto", "revolucionário", "incrível". Quando
houver uma regra, dê o motivo em uma linha.

---

# 2. As regras inegociáveis

Estas seis não se negociam. As outras regras deste documento têm contexto; estas não.

### 2.1 Grafia: `e-A` e `e-Auditoria`, nunca `ë-A`

O trema existe no **desenho do logotipo**, não na palavra escrita. Em texto corrido é
sempre `e-A` e `e-Auditoria`.

### 2.2 Nome sozinho vira logotipo

Quando o nome aparecer **fora de uma oração** — cabeçalho, rodapé, assinatura, selo,
rótulo de coluna, qualquer aplicação isolada — use a **imagem do logotipo**, não a palavra.
A palavra escrita só sobrevive dentro de frase.

### 2.3 Sub-marca não carrega a marca-mãe

**Não existe** o lockup `Sub-marca | e-Auditoria`. Essa construção não está na identidade
e nem na tipografia institucional. Toda sub-marca é autossuficiente. A assinatura da
e-Auditoria só entra junto quando a solicitação de produção pedir explicitamente.

### 2.4 Expressões que nunca quebram linha

`e-Auditoria` · `Simples Nacional` · `Simples Híbrido` · `Lucro Real` ·
`Lucro Presumido` · `Reforma Tributária`

No HTML: `<span class="ea-nb">…</span>` (a classe aplica `white-space:nowrap`).
Em código de exemplo: `&nbsp;` entre as palavras.

**E vão com inicial maiúscula mesmo quando aparecem sozinhas:** "o Simples", "a Reforma".
São nomes próprios do domínio fiscal. Minúscula só quando for mesmo o adjetivo
("de forma simples").

### 2.5 CTA é âmbar com texto navy

`background: #FEC008` · `color: #050634` · formato **pílula** (`border-radius:100px`).
Um único CTA amarelo por dobra. Salvo exceção explícita de projeto ou vertical.

**Por quê:** navy sobre âmbar dá **11,8:1** de contraste. Branco sobre âmbar dá **1,65:1** —
reprova em qualquer critério e some no sol da tela do celular. Não é escolha estética.

### 2.6 A marca-mãe fala em azul

Quando o assunto é a **e-Auditoria**, a paleta é **azul e no máximo lilás**. Pink, laranja
e magenta só quando o assunto for uma sub-marca ou vertical que os tenha.

---

# 3. A marca

## 3.1 As três formas

| Forma | Quando usar |
|---|---|
| **Horizontal** | O padrão. Sempre que houver largura disponível: header de site, rodapé, topo de e-mail, capa de apresentação, assinatura de peça. |
| **Vertical** | Espaços quadrados, pouca largura, selo. |
| **Símbolo** (o "e" com três pontos) | Favicon, foto de perfil de rede social, ícone de app, marca d'água, assinatura reduzida. **Nunca substitui a assinatura completa na primeira aparição da marca numa peça.** |

## 3.2 Cor do logotipo — o ponto delicado

O azul do **logotipo** é `#2B2E6F` (um índigo escuro).
O azul primário de **interface** é `#2F24FF`.

**São cores diferentes, e isso é intencional. Não normalize uma pela outra.**
Logotipo usa `#2B2E6F`. Interface e CTA usam a paleta de UI.

## 3.3 Versões de arquivo

Horizontal e vertical existem em **azul**, **preto** e **branco**. A branca é para fundo
escuro ou sobre foto.

**Sobre os arquivos:** os originais eram PNG pequeno (o horizontal tinha 641×75 px). Foram
**vetorizados** (marching squares + Douglas-Peucker, fidelidade medida entre 0,10% e 0,25%
na resolução nativa). Os SVGs estão em `assets/marca/`.

Ressalva honesta: vetorização é reconstrução, não o arquivo original. Para impresso de alta
exigência (offset, sinalização grande), peça o `.ai`/`.eps` ao estúdio que fechou a marca.
Para tela, web e apresentação, resolve — e é infinitamente melhor que ampliar o PNG.

## 3.4 Área de respiro e tamanho mínimo

- **Respiro:** a altura do "e" do símbolo em volta de toda a assinatura, nos quatro lados.
- **Tamanho mínimo em tela:** 24px de altura para a horizontal, 16px para o símbolo.

## 3.5 O que nunca fazer

- Distorcer, girar ou aplicar sombra
- Trocar a cor fora das três versões oficiais
- Colocar sobre fundo de baixo contraste
- Reescrever o nome com outra fonte
- **Quebrar a palavra "e-Auditoria" em duas linhas**
- Montar lockup com sub-marca (ver 2.3)

---

# 4. Cor

## 4.1 Paleta de marca

```
#050634  navy / ink — fundo escuro, texto forte
#2F24FF  íris — primária de UI, botões e links
#4F45F5  violeta
#772BF2  roxo de vertical
#2488FF  azul coringa — une as verticais
#00FFEA  ciano — acento de DADOS sobre fundo escuro. Nunca dominante.
#FEC008  CTA amarelo — cor única de ação
#FB5507  laranja — energia, "ao vivo"
#FF0071  pink — expressivo
#FF2F34  vermelho — alerta, urgência
#2B2E6F  azul do LOGOTIPO (ver 3.2)
```

## 4.2 Neutras

```
#FFFFFF branco    #F5F9FC branco gelo    #A2B9DA borda
#576B86 texto secundário    #1E2126 grafite    #E4E9F5 divisor
#000000 preto (uso restrito)
```

## 4.3 Pastéis — "pastel é palco, cor plena é ator"

```
#E7E2FF lilás    #DFE2FF peri    #DBE7FF azul    #EFE6FF lavanda
#FFF0C4 baunilha    #D9F5F0 ciano    #F0E3FF uva    #FFE1F0 rosa
```

## 4.4 Gradientes oficiais — use as receitas, não invente

```
texto/palavra    135°  #4F45F5 → #8439E6
tri-tom          125°  #2F24FF → #8439E6 (55%) → #FF0071
dados/tech        90°  #00FFEA → #4F45F5 → #8439E6
fundo escuro     140°  #06063A → #0D0540 (50%) → #1C0860
fundo claro      220°  #DDD6FE → #C7DBFF (48%) → #E5DAFF
aurora           135°  #D8E8FF → #EEEAFF → #F8E8FF → #FFF8EE
masthead e-mail  122°  #8439E6 → #5B4BF2 (46%) → #2488FF   (fallback sólido #4F45F5)
CTA âmbar        125°  #F7A70A → #FEC008 (48%) → #FFD65C
ao vivo          135°  #FB5507 → #FF2F34
```

**As paradas dos gradientes são tokens tanto quanto as cores chapadas.**

## 4.5 Paletas por vertical

Extraídas por amostragem de pixel das artes oficiais. **A proporção medida é a proporção
de uso recomendada** — é a regra 60-20-10 aplicada de verdade.

| Vertical | Cores e proporção |
|---|---|
| **Integrar** | `#772BF2` 66% · `#4F45F5` 34% |
| **Atualizar regras fiscais** | `#00FFEA` 39% · `#2486FF` 39% · `#2F24FF` 21% |
| **Auditar arquivos** | `#2F24FF` 39% · `#2486FF` 39% · `#050634` 21% |
| **Recuperar crédito** | `#2486FF` 39% · `#2F24FF` 39% · `#00FFEA` 21% |
| **Reforma Tributária** | `#2486FF` 40% · `#772BF2` 22% · `#4F45F5` 19% · `#00FFEA` 19% |
| **Corrigir SPED** | `#772BF2` 40% · `#2486FF` 39% · `#4F45F5` 21% |

## 4.6 Paletas claras (pastel)

Campanhas com pastel vêm dando bom resultado. Cada vertical tem uma escala clara derivada:
fundo de seção quase branco, pastel de superfície, pastel de realce, e a cor plena como
acento.

**Regra:** pleno para acento, dado e CTA. Pastel para superfície e fundo de seção.

Referências verificadas em produção: as LPs do **Simulador da Reforma para o
Simples Nacional** e do **Planejamento Tributário na Reforma** — as duas são campanhas
filhas da vertical Reforma Tributária.

## 4.7 Cores de sub-marca

Não devem ser normalizadas para o token mais próximo. São da identidade delas.

```
#0051FF  Programa de Parcerias
#5243FA  Imersão e-A
```

---

# 5. Tipografia

Duas famílias, só.

- **Familjen Grotesk** — títulos, números, display. Peso **700**. **Nunca itálico.**
  Tracking `-0.02em`.
- **Manrope** — corpo, CTA, rótulos. Pesos **400 a 600**.

```css
@import url('https://fonts.googleapis.com/css2?family=Familjen+Grotesk:wght@400;500;600;700&family=Manrope:wght@400;500;600;700&display=swap');
```

## Escala fluida

```
display   clamp(2.5rem, 5vw + 1rem, 5.25rem)     40 → 84px   hero
h1        clamp(2.25rem, 4vw + 0.5rem, 4rem)     36 → 64px
h2        clamp(1.75rem, 3vw + 0.5rem, 3.625rem) 28 → 58px
h3        clamp(1.375rem, 1.5vw + 0.5rem, 2rem)  22 → 32px
número    clamp(2.5rem, 4vw + 0.5rem, 4rem)      40 → 64px   âncora
lead      clamp(1.0625rem, 0.6vw + 0.9rem, 1.1875rem)  17 → 19px
corpo     1rem (16px)      pequeno 0.875rem (14px)     eyebrow 0.75rem (12px)

altura de linha: 1.05 títulos · 1.3 intermediário · 1.6 corpo
tracking: -0.02em títulos · 0.12em eyebrow em maiúsculas
```

**Em e-mail** a pilha termina em Arial:
`'Manrope','Helvetica Neue',Helvetica,Arial,sans-serif`. A fonte da marca não carrega em
vários clientes — mas cai *bem*, e onde carrega o e-mail fica com a cara da casa.

---

# 6. Geometria, espaço e movimento

## Raio
```
12px  chip, imagem de e-mail
20px  card
28px  card grande
40px  seção, painel
100px / 999px  pílula, botão
```

## Sombra
```
sm  0 4px 24px rgba(5,6,52,.08)
md  0 12px 40px rgba(60,40,140,.14)
lg  0 32px 80px rgba(47,36,255,.22)
glow do CTA  0 10px 26px rgba(254,192,8,.34)
```

**A sombra acompanha a cor do objeto.** Botão âmbar leva sombra âmbar; com a violeta sobra
um halo roxo embaixo de um botão amarelo.

## Espaço — escala base 8px
```
4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96
respiro de seção: clamp(4rem, 9vw, 7.5rem)
container: 1180px
```

Use `gap` em flex/grid, **não** `margin` por elemento — margem colapsa e duplica em
silêncio, e é a origem mais comum de "por que essa seção tem espaço a mais embaixo".

## Movimento
```
easing  cubic-bezier(.16, 1, .3, 1)
durações  0.2s rápido · 0.4s padrão · 0.8s lento
```

Tudo atrás de `prefers-reduced-motion`. Animação só em `transform` e `opacity` — são as
duas propriedades que o compositor do navegador resolve sozinho, sem recalcular layout.

---

# 7. Ícones

## 7.1 Ícones 2D — o padrão

**SVG inline.** Não depende de CDN, herda a cor por `currentColor`, escala sem serrilhar e
custa ~200 bytes.

```
viewBox 24×24 · stroke-width 1.75 · fill none
stroke-linecap e stroke-linejoin: round
cor por currentColor
```

- Ícone **nunca carrega informação sozinho** — sempre acompanha um rótulo.
- Decorativo leva `aria-hidden="true"`.
- Ícone que é o único conteúdo de um botão leva `aria-label`.
- **Dentro de botão, largura e altura explícitas** (16px). Se o CSS de escopo cair, o SVG
  não incha. Isso já aconteceu em produção: SVGs de 340px numa página publicada.

## 7.2 Ícones 3D

Para **destaque, hero, card de topo e social**. Nunca em UI funcional, nunca misturado com
o set 2D na mesma grade, nunca abaixo de 48px.

Padrão visual: luz do canto superior esquerdo, material de vidro/plástico, paleta da marca,
sombra de contato, fundo transparente.

**Fontes mapeadas:** Fluent Emoji da Microsoft (github.com/microsoft/fluentui-emoji,
licença MIT — seguro para uso comercial) e o kit "Apple Emojis in 3D" da BRIX no Figma
Community (conferir termos antes de uso comercial).

---

# 8. Superfícies: padrões, fundos e vidro

## 8.1 Padrões

Reautorados como **SVG tileável** (~600 bytes cada), recoloríveis por `currentColor`:
malha fina, malha marcada, pontos, pontos com cruz, barras na diagonal, paralelogramos.

**Regra:** padrão é textura de fundo, **nunca competidor do conteúdo**.
Opacidade típica: **0,05 a 0,12** sobre claro · **0,06 a 0,15** sobre escuro.

## 8.2 Backgrounds

Cinco receitas reproduzíveis em CSS: aurora clara, noite profunda, malha + auréola, vidro
sobre cor, e ruído/grão.

**Regras:** contraste do texto manda. Fundo em imagem nunca acima de ~40 KB. Preferir CSS
a imagem sempre que o resultado for equivalente. Em fundo escuro, o texto vem do token de
texto-sobre-escuro, não branco puro. Degradê em CSS é gratuito; imagem grande em hero
compete com o LCP.

## 8.3 Vidro

Decomposto em camadas nomeadas: fundo que atravessa, tint, desfoque, borda de luz,
realce superior, sombra projetada, aberração cromática nas bordas.

**Escala de três níveis:** sutil (UI, card de conteúdo) · médio (destaque, painel sobre
imagem) · pesado (hero, forma decorativa). Os valores mudam entre fundo claro e escuro.

**Prioridade:** os modelos de vidro **já usados nas landing pages anteriores** têm
precedência sobre qualquer variação nova. Vidro novo é complemento, não substituto.

**Regras duras:** `backdrop-filter` custa caro — no máximo **2 superfícies de vidro
simultâneas** na viewport, **nunca vidro sobre vidro**, sempre um fallback sólido
(`@supports not (backdrop-filter: blur(1px))`). Contraste de texto sobre vidro precisa ser
medido com o **pior fundo possível**, não com o fundo do mockup.

---

# 9. Sub-marcas e programas

Cada uma tem identidade própria **e é autossuficiente** (ver regra 2.3).

| Programa | O que caracteriza | Cor própria |
|---|---|---|
| **Imersão e-A** | Pílula com **borda em degradê** ciano→azul→violeta, sparkle de 4 pontas, círculo branco com "e-A". Fundo pastel arejado. Pílula secundária "online e gratuito" em navy. | `#5243FA` |
| **Aulão e-A** | Motivo de **player de mídia**: botão de play circular + pílula. Elementos de apoio são controles de transporte e barra de progresso. Fundo azul→violeta→magenta. CTA amarelo. | — |
| **Radar Tributário** | Ícone de app com sparkline (pulso de radar) + wordmark em duas linhas. Fundos de bolhas suaves em lavanda e azul. Versões: preta, branca, degradê. | — |
| **O Jogo da Contabilidade** | Símbolo em quadrado arredondado com figura + wordmark. Variante "da Reforma" para a temporada. **Único território dominantemente escuro e cinematográfico** — é programa gravado. Selos "NOVO EPISÓDIO" e "AO VIVO". | — |
| **Arena Fiscal** | Símbolo de Coliseu + wordmark. Colorido em degradê ciano→azul→violeta. | — |
| **Programa de Parcerias** | Selo quadrado "Parceiro Oficial". **6 versões oficiais em SVG**: padrão, secundária, versão branca, negativa, outline, outline branca. | `#0051FF` |
| **Jornada do Especialista** | Tema completo, **logotipo em proposta** (aguardando aprovação). Motivo de turmas manhã/tarde (☀️/🌙), countdown, stepper gamificado. | — |
| **PremIA** | Projeto **interno** do time de desenvolvimento. Wordmark com "IA" destacado. **Não vai para cliente.** | — |
| **Autores Tributários** | Projeto da redação. Fundo azul forte, tipografia grande, troféu amarelo, elemento 3D violeta. | — |

## Armadilha ao usar SVG oficial de sub-marca

Os arquivos exportados do Illustrator usam as **mesmas classes** (`.cls-1`, `.cls-2`…) com
cores diferentes em cada um. Inline na mesma página, **a última regra vence e todos os
logotipos ficam com a cor do último** — o logo aparece, só que errado, sem nenhum aviso.

Solução: renomeie as classes por arquivo, ou use `<img src="...svg">` em vez de inline.

---

# 10. Mascotes

## e-Bot — mascote da e-Auditoria

Robô 3D azul/lilás, corpo arredondado, antena com esfera, olhos retangulares ciano em visor
escuro, segurando um tablet com o símbolo da marca. Corpo `#C7D3FF`, olhos `#38D1FF`.

**Papel:** guia do produto. Explica funcionalidade, aparece em onboarding e tutorial.

## Incendiária — mascote da equipe Incendiários (vendas)

Chama-personagem 3D com rosto kawaii, degradê amarelo→laranja→vermelho, olhos grandes
castanhos. Laranja de referência `#FF4F00`.

**Papel:** energia do time comercial. Campanha interna, ranking, celebração de meta.
**Nunca em material institucional para cliente.**

## Regras para os dois

- Mascote **nunca cobre informação**.
- **Nunca** em peça de compliance ou jurídica.
- **Nunca** redesenhado ou recolorido fora da paleta dele.
- Formatos: PNG com transparência (peça estática, social, apresentação) e WebP (web).
  SVG e Lottie são **pendentes** — o mascote hoje é render 3D; virar vetor exige redesenho.
- Kit de motion definido: *idle* (respiração/flutuação), *entrada* (escala com leve
  overshoot), *atenção* (pulso). Tudo só com `transform` e `opacity`, desligado em
  `prefers-reduced-motion`.

---

# 11. Componentes web

O catálogo tem **155 blocos** com preview e código. Antes de criar um bloco novo, verifique
se ele já existe.

**Primitivos:** botões (CTA, primário, outline, ghost), badges e eyebrows, card de vidro,
divisores, contador animado, scroll-reveal, fundos e orbs.

**Blocos de landing page:** header (3 variantes), heros (split com formulário, centrado com
tela do produto, evento), barra de prazo, fachada de vídeo, faixa de logos, faixa de
números, grid de benefícios, media & texto, passos, antes × depois, abas acessíveis,
depoimentos, bento, FAQ com JSON-LD, card de captura, CTA final, CTA sticky mobile.

**Padrões de evento:** countdown, agenda + turmas manhã/tarde, grade de palestrantes,
transmissão ao vivo.

## Detalhes que importam

- **Contador:** o valor final **já está escrito no HTML**; o JS só o substitui para animar.
  Sem JS, o número correto continua lá. Formate com `toLocaleString('pt-BR')`.
- **Scroll-reveal:** a classe que esconde é posta **pelo JS** (`.is-armed`), nunca no CSS
  estático. E **o que já nasce visível não ganha fade** — título, subtítulo e CTA do hero
  entram prontos. Reveal só faz sentido abaixo da linha d'água.
- **Passos:** só numere quando a ordem **for real**. Use `<ol>` de verdade — leitor de tela
  anuncia "item 2 de 3" sozinho.
- **Fachada de vídeo:** a página carrega só a capa + botão; o player entra no clique.
  Tira ~1 MB e várias requisições de terceiro do carregamento. Autoplay **só no desktop**
  e sempre mudo.
- **Captura:** um só por página, com `id="agendar"`. Todos os CTAs apontam para essa
  âncora — trocar o formulário vira mexer em um lugar só.

---

# 12. Dataviz fiscal

O diferencial que não se copia rápido: mostrar número fiscal de um jeito que o contador
entende em três segundos. Tudo em HTML/CSS/SVG — responsivo, nítido em qualquer tela, sem
depender de upload.

**KPI cards** · **donut em `conic-gradient`** (CSS puro, zero biblioteca) ·
**tabela de alíquotas antes × depois** com status pills · **gráfico de ponto de virada** ·
**moldura de produto** (janela de navegador em volta do print).

## Regras

- Tabela é o formato que o contador mais confia. **Não substitua por gráfico só por
  estética.**
- Números alinhados com `font-variant-numeric: tabular-nums`.
- Tabela larga tem rolagem própria (`overflow-x:auto`) — o body da página nunca rola de lado.
- **Status nunca é só cor:** a pílula sempre carrega texto.
- Donut é imagem semântica: `role="img"` + `aria-label` com o número por extenso.
- **Todo número ilustrativo precisa dizer que é ilustrativo** — no próprio card, não só no
  rodapé. E nunca use nome de empresa real num exemplo inventado.
- **Cor de série é compromisso com o produto.** Se a interface usa roxo para Lucro
  Presumido, a LP usa roxo para Lucro Presumido.
- Sempre `aspect-ratio` + `width`/`height` na imagem — reserva o espaço e zera o CLS.

---

# 13. E-mail

Mundo técnico separado. **Tabelas e estilos inline**, nunca flexbox, nunca `var()` — o
Outlook não entende.

```
larguras: 640px o e-mail · 560px imagem cheia · 436px dentro de card
raios: cartão 24 · cards 20 · imagens 14–16 · pílulas 100
```

- Gradiente **sempre** com `bgcolor="#..."` sólido de fallback.
- Botão bulletproof: `<td bgcolor>` + `<a>` + `<span style="color:… !important">`.
- **Preheader oculto** logo após o `<body>` — é o texto que a caixa de entrada mostra ao
  lado do assunto.
- Rodapé com razão social, endereço e `{{ unsubscribe_link }}` com
  `data-unsubscribe="true"`.
- Marcador de lista é **célula de tabela**, não emoji — emoji vira quadrado vazio em alguns
  clientes.

## Cores de e-mail
```
#E7ECF6 moldura   #F1F2FF card claro   #4A4D6B corpo
#576B86 texto secundário
```

⚠️ **Não use `#7377A0`.** Dá 4,31:1 sobre branco e reprova AA para texto pequeno.

## Sistema de impacto (newsletter Radar Tributário)
```
alto         bg #FFE7E7 / txt #C7202B  🔴
médio        bg #FFF3D1 / txt #9A6A00  🟡
operacional  bg #E2EEFF / txt #1667D6  🔵
```
A legenda do código de cor entra **uma vez por edição**, perto do primeiro item.

## Modelos existentes

Doze modelos de arrastar-e-soltar no HubSpot (o ID do portal está no gerenciador de senhas da equipe). **Não aparecem em
`hs cms list`** — só templates codificados aparecem. Para alcançá-los:

```
hs api "/content/api/v2/templates?limit=300"
hs api "/content/api/v2/templates/<id>"
```

O tema **`ea-lm-2026`** é o modelo padrão de nutrição, codificado — a fusão do "Modelo LM 1"
(estrutura) com o "Modelo LM 2" (disciplina de cor), mais 8 correções. Passa 6/6 na prova
de fogo; os originais passavam 2/6 e 1/6.

---

# 14. Regras de produção

Bloco HTML no WordPress (tema GeneratePress). **Cada uma corresponde a algo que já quebrou
no ar.** Não são estilo.

1. **Zero `&&` no JavaScript.** O editor recodifica o caractere e derruba o script inteiro.
   Use `if` aninhado. Vale até dentro de comentário.
2. **Escopo por wrapper único.** Todo CSS prefixado por uma classe da peça. Nunca seletor
   global.
3. **Nenhum `data-*` no wrapper de escopo.** O sanitizador apaga `data-*` e, nesse elemento,
   leva `class` e `id` junto. Só `class` e `id` sobrevivem.
4. **Nenhuma regra de estado normal dependendo de `[data-*]`.**
5. **Prefixo do wrapper também dentro de `@media`.** Media query não soma especificidade.
   *(Regra do WordPress. Em e-mail, classe solta dentro de `@media` é o padrão correto.)*
6. **Cor de texto em `<a>` precisa de `!important`.** O tema tem
   `.inside-article a{color:initial !important}`. **Corolário:** botão sobre fundo escuro
   não pode depender de texto claro — use fundo âmbar com texto navy.
7. **Arquivo de entrega sem comentário.** Um `*/` órfão engole o bloco seguinte em silêncio.
8. **`@import` na linha 1**, nada acima — o editor promove ao topo e descarta o que vinha antes.
9. **Fail-safe sem JS.** Conteúdo e números pré-preenchidos; o JS só anima.
10. **Captura sempre por embed HubSpot** (portal da e-Auditoria). Nunca form próprio, nunca
    chave de API no front. **Confira o `data-form-id`** — é o erro silencioso mais caro.
11. **Validar na página publicada**, nunca no preview do editor.
12. **Colar no campo de código de UM bloco**, nunca no canvas — o Gutenberg quebra em
    vários blocos e duplica o wrapper.
13. **Template da página em Full Width**, sem barra lateral — o full-bleed depende disso.
14. **Full-bleed só no wrapper:** `width:100vw; margin-left:calc(50% - 50vw)`, com
    `overflow-x:clip` (**nunca `hidden`** — cria contêiner de rolagem e mata o `sticky`).

## O teste de 10 segundos

Quando um bloco vai ao ar sem estilo, **não olhe o CSS primeiro. Olhe se o wrapper ainda
tem a classe:**

```js
document.querySelector('.ea-lp')   // null? achou o problema.
```

---

# 15. Acessibilidade

Combinações já medidas que **reprovam**:

| Combinação | Contraste | Situação |
|---|---|---|
| Ciano `#00FFEA` como texto sobre branco | 1,27:1 | reprova — ciano só sobre escuro |
| `#2F24FF` como texto sobre navy | 2,60:1 | reprova — azul primário só sobre claro |
| `#7377A0` sobre branco | 4,31:1 | reprova em texto pequeno |
| Branco sobre âmbar `#FEC008` | 1,65:1 | reprova |
| **Navy `#050634` sobre âmbar** | **11,8:1** | ✅ é o padrão do CTA |

Outras regras: ícone nunca carrega informação sozinho · status nunca é só cor · foco pelo
teclado sempre visível · `prefers-reduced-motion` respeitado · `alt` descritivo em imagem
que informa, `alt=""` em imagem decorativa.

---

# 16. CRO

## Instrumentar antes de testar

Sem isto, nenhum teste é legível: **scroll depth por dobra** · **clique de CTA por seção** ·
**início × envio do formulário** (separa "ninguém chega" de "chega e desiste") ·
**play e tempo assistido do vídeo** · **cliques em elemento interativo**.

## Princípios

- **Amostra pequena não sustenta teste pequeno.** LP B2B de nicho não dá significância para
  testar cor de botão em três semanas. Priorize mudanças grandes e método qualitativo.
- **O calendário manda.** Campanha com janela fiscal tem data de congelamento.
- **Copy com prazo tem data de morte.** Contador de dias vira erro factual quando a janela
  fecha. É manutenção obrigatória, não teste.
- **CTA repetido demais anestesia.** Menos CTAs, em pontos de scroll medido, com verbos
  distintos. Olhe clique bruto **e** conversão juntos.
- **Prova concreta bate argumento.** Um gráfico que mostra o mecanismo vale mais que quatro
  dobras afirmando que ele existe.
- **Número inventado custa confiança.** Um caso real anonimizado converte melhor e reduz risco.
- **Mobile primeiro na hora de validar.** É pré-requisito, não teste.
- **Um teste por vez.**

---

# 17. Como verificar uma peça

Existe um verificador de conformidade. Ele confronta a peça contra o sistema **sem opinião**:

```
python ferramentas/prova-de-fogo.py <arquivo-ou-pasta>
python ferramentas/prova-de-fogo.py <pasta> --email
python ferramentas/prova-de-fogo.py <arquivo> --json
```

Mede seis critérios: **cor** (ΔE00 de cada hexadecimal contra a paleta inteira) ·
**tipografia** (resolve `var()` antes de julgar) · **CTA** · **contraste WCAG** ·
**produção** (as armadilhas acima) · **marca** (grafia e proteções de quebra).

Sai com código 0 se passou em tudo. Serve em automação.

**Rode antes de entregar.** Foi ele que descobriu que o `#7377A0` estava reprovando AA em
produção há meses, sem ninguém ter medido.

---

# 18. Pendências conhecidas

Registradas com honestidade, para ninguém tropeçar nelas:

- **`#772BF2` vs `#8439E6`** — o roxo que aparece nas artes não é o tokenizado. ΔE00 = 3,19,
  é visível. Recomendação: redefinir `--ea-purple` para `#772BF2`. Muda três gradientes.
- **`#2486FF` vs `#2488FF`** — ΔE00 = 0,71, ruído de exportação. Normalizar.
- **`#7377A0`** — reprova AA. Revisar o tema `ea-radar-news-2026`.
- **Logotipo vetorizado, não original** — para impresso de alta exigência, pedir o `.ai`.
- **SVG e Lottie dos mascotes** — pendentes; exigem redesenho vetorial.
- **Logotipo da Jornada do Especialista** — três propostas feitas, aguardando aprovação.
- **Set de vidro em SVG** — em avaliação.
- **Componentes React para o registry shadcn** — decisão do time de produto.

---

*Documento gerado em 31/07/2026. Fonte da verdade dos tokens: `eauditoria-tokens.css`.
Catálogo visual: https://design.e-auditoria.com.br/catalogo.html*
