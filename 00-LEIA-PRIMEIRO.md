---
projeto: Design System e-Auditoria
status: v4 entregue — catálogo, tokens, assets, skill e registry
atualizado: 2026-08-21
confidencialidade: material proprietário — repositório privado, site com acesso controlado
autoria: Tamires Fernandes — equipe de Criação da e-Auditoria
responsável: equipe de Criação (dona do banco de elementos)
---

# 🎨 Design System e-Auditoria — comece por aqui

Esta é a pasta única do projeto. Se você (ou o Claude) está retomando o trabalho,
leia este arquivo primeiro: ele diz onde paramos e o que vem a seguir.

---

## ⛔ REGRA INEGOCIÁVEL DA MARCA

**A palavra "e-Auditoria" NUNCA, EM HIPÓTESE ALGUMA, pode ser quebrada** — nem por
hífen, nem por quebra de linha entre "e-" e "Auditoria". Em todo HTML, envolver o
nome em `<span class="ea-brand">e-Auditoria</span>` (a classe aplica `white-space:nowrap`).
Isso já está no `eauditoria-tokens.css` e no catálogo.

---

## ⛔ ESTE MATERIAL NÃO É PÚBLICO

O catálogo reúne logotipo, sub-marcas, mascotes e peças de campanha. O risco não é
vazamento de segredo — é **reprodução da marca por terceiros** e cópia do sistema por
outros times de design.

- Repositório **privado**, sempre.
- Site **atrás de autenticação**, mesmo para consulta.
- Fornecedor recebe acesso **nominal**, revogado no fim do contrato.
- Arte-master (vetor editável, arquivo Adobe, mascote em alta) **não entra no repositório**.

Detalhe em `COMO-PUBLICAR.md`.

---

## O que está nesta pasta

| Arquivo | O que é |
|---|---|
| `00-LEIA-PRIMEIRO.md` | Este arquivo — status e próximos passos. |
| `01-inventario-mestre.md` | Inventário completo dos 110+ componentes já existentes, em 6 camadas. |
| `eauditoria-tokens.css` | **A pedra fundamental.** Arquivo único de tokens (cor, tipografia, espaço, raio, sombra, gradientes). Namespace `--ea-*`. Inclui tabela de equivalência para e-mail. |
| `catalogo.html` | Fonte do catálogo vivo (edita aqui e republica). |
| `_extracao-bruta/` | Backups das extrações por projeto (Parcerias, Jornada, Nova News). |
| `PENDENCIAS.md` | O que ainda precisa de decisão da Criação. |
| `COMO-PUBLICAR.md` | Onde o material fica hospedado e **quem pode ver**. |

**Catálogo publicado (acesso restrito — solicite à Criação):**
https://design.e-auditoria.com.br/catalogo.html

**PÁGINA ÚNICA — decisão da liderança de Criação em 31/07/2026.** Chegamos a dividir em 9 páginas para
resolver o peso (5,7 MB), e funcionou tecnicamente, mas **quebrou a leitura de sistema**: a
Criação navega o catálogo procurando relação entre as partes, e isso se perde quando cada
parte mora num endereço. A decisão foi voltar para uma página só, mesmo pesada.
Estado atual: **66 seções, 154 blocos, 91 imagens, 3,6 MB**.

O peso foi reduzido de 5,7 para 3,6 MB sem tirar conteúdo: reencodamos tudo em WebP com
orçamento por **papel** da imagem (logotipo tolera pouco, referência de galeria tolera
muito, textura tolera mais ainda). Ver `assets/LEIA-ME.md`.

A pasta `_paginas-legado-multipagina/` guarda a versão dividida, caso um dia se decida
hospedar de verdade — aí o problema de peso some (imagem vira arquivo, não data URI) e a
divisão passa a ser opcional, não remédio.

Montagem: `montar_pagina_unica.py` a partir de `catalogo-v2.bak.html` + fragmentos de
seção + `assets/manifest.json`.

---

## Onde paramos (v1 — feito ✅)

1. **Viabilidade confirmada:** a e-Auditoria já tem uma biblioteca madura, só fragmentada. O trabalho é unificar, não criar do zero.
2. **Diagnóstico central:** a mesma cor de marca estava redeclarada com 5 nomes diferentes (`--ea-*`, `--r-*`, `--c-*`, `--color-*`, `--cp`). Resolvido no arquivo de tokens.
3. **Extração completa** de 6 LPs WordPress + 32 módulos HubSpot (Parcerias, Jornada, Nova News) + brandbook + guia técnico → `01-inventario-mestre.md`.
4. **Tokens canônicos** criados (`eauditoria-tokens.css`).
5. **Catálogo vivo v1** publicado: fundações (cor, gradiente, tipo, geometria) + primitivos (botões, badges, card de vidro) + blocos-assinatura web (stats, features, CTA) e e-mail (botão bulletproof, âncora de prazo, lista de artigos) + regras de governança. Cada bloco com preview + código para copiar.

---

## Onde paramos (v2 — feito ✅ · 31/07/2026)

O catálogo saiu de 13 para **40 blocos**, em 49 seções. O que entrou:

1. **Fundações completas** — espaçamento (era o único grupo de tokens que não existia
   em lugar nenhum) e **sistema de ícones**, que paga o débito nº 2: o padrão passa a ser
   **SVG inline** (24×24, traço 1.75, `currentColor`), com um set base de 12 ícones.
   Aposentados Font Awesome e emoji-como-ícone — a única exceção é o par ☀️/🌙 das
   turmas da Jornada, que é motivo de marca, não ícone de interface.
2. **Primitivos** — divisores (web + e-mail), contador com fail-safe, scroll-reveal com
   a regra de "acima da dobra entra pronto", fundos/orbs.
3. **Blocos web (17)** — header, 3 heros, barra de prazo, fachada de vídeo, faixa de
   logos, media&texto, passos, antes×depois, abas acessíveis, depoimentos, bento, FAQ
   com JSON-LD, card de captura, CTA final e CTA sticky mobile.
4. **Dataviz fiscal (5)** — KPIs, donut em `conic-gradient`, tabela de alíquotas com
   status pills, **gráfico de ponto de virada** e moldura de produto.
5. **Padrões de evento (4)** — countdown, agenda + turmas dia/tarde, palestrantes,
   transmissão ao vivo.
6. **E-mail completo (7)** — masthead, botão bulletproof, âncora de prazo, lista de
   artigos, card de evento, enquete e rodapé de conformidade.
7. **Governança de 7 → 14 regras.** As sete novas vieram do desastre de publicação de
   29/07/2026 (ver `../GUIA-BLOCO-HTML-PERSONALIZADO.md`): nada de `data-*` no wrapper,
   estado normal não depende de atributo, prefixo também dentro de `@media`, cor de `<a>`
   com `!important`, arquivo de entrega sem comentário, `@import` na linha 1, validar no
   ar e não no preview.
8. **Duas seções novas de processo** — **Pré-voo** (checklist + roteiro PowerShell +
   validação no console da página publicada) e **CRO** (o que instrumentar antes de
   testar e os princípios que já valem para o próximo projeto).

Cada bloco com armadilha conhecida traz o aviso no próprio card, e onde há decisão de
conversão envolvida há uma nota de CRO — para o aprendizado viajar junto com o código.

---

## Onde paramos (v3 — feito ✅ · 31/07/2026)

O catálogo deixou de ser só de componentes e passou a cobrir **identidade**. De 40 para
**104 blocos**, em 58 seções. Fonte: `2025/Nova IDV/Brandbook/Apresentação/Links`.

1. **Uso da marca** — assinatura horizontal, vertical e símbolo, nas 4 versões, com área de
   respiro, tamanho mínimo, aplicações do símbolo (favicon, perfil, app) e usos proibidos.
2. **O vetor do logotipo passou a existir.** Os arquivos oficiais eram PNG de 641×75 px.
   Vetorizamos por marching squares + Douglas-Peucker e medimos a fidelidade rasterizando
   de volta (0,35% a 2,66% de divergência). Detalhe e ressalvas em `assets/LEIA-ME.md`.
   O botão de PNG do catálogo **gera o arquivo na hora a partir do vetor**, em canvas.
3. **Sub-marcas** — Arena Fiscal e Imersão e-A, com as versões preta e branca geradas
   (não existiam no material de origem) e regra de convivência com a marca-mãe.
4. **Mascotes** — e-Bot e Incendiária, com ficha de personalidade, formatos por uso e um
   kit de motion em CSS (idle, entrada, atenção).
5. **6 paletas por vertical**, extraídas por amostragem de pixel das artes oficiais, com a
   proporção medida virando proporção de uso, e contraste WCAG calculado por cor.
6. **Superfícies** — Padrões (reautorados como SVG tileável, ~600 bytes cada, recoloríveis),
   Backgrounds (galeria de inspiração + 5 receitas reproduzíveis em CSS) e Vidro (anatomia
   em camadas, escala de 3 níveis, formas em CSS/SVG).
7. **Ícones separados em 2D e 3D.** O set 2D foi ampliado; o 3D ganhou regras de uso e um
   set alternativo em SVG, para não depender de PNG de banco de imagem.
8. **Logotipo no topo do menu**, em SVG, herdando a cor do tema.

### Decisões de token em aberto (precisam de você)
Todas as diferenças abaixo foram medidas com **ΔE00 (CIEDE2000, D65)**, não a olho.

- **Azul do logotipo `#2B2E6F` ≠ azul de UI `#2F24FF`.** Documentado como intencional no
  catálogo. Confirmar se é isso mesmo ou se um dos dois deve mudar.
- **`#2486FF` (paletas) vs `#2488FF` (token) → ΔE00 = 0,71.** Abaixo do limiar de
  percepção (~1,0); é desvio de 2 no canal azul, ou seja, ruído de exportação.
  **Recomendação: normalizar para `#2488FF`, sem criar token novo.**
- **`#772BF2` (paletas) vs `#8439E6` (token `--ea-purple`) → ΔE00 = 3,19.** É visível,
  não é ruído. E o `#772BF2` domina duas verticais, enquanto o `#8439E6` **não apareceu
  em nenhuma amostragem das artes oficiais**. **Recomendação: redefinir `--ea-purple`
  para `#772BF2` e aposentar `#8439E6`**, em vez de acrescentar um sétimo token.
  ⚠️ Isso muda gradientes existentes (`--ea-grad-text`, `--ea-grad-text-tri`,
  `--ea-grad-masthead`) — decidir antes de mexer.

### Cores de sub-marca que não estão nos tokens (levantadas por medição)
- **`#0051FF`** — azul do selo do Programa de Parcerias. ΔE ≈ 9 do violeta mais próximo:
  é cor própria do programa, **não normalizar**. Entra como token de sub-marca.
  (O navy do selo, `#2B2E6F`, é exatamente o azul do logotipo — a ligação entre as duas
  marcas é essa, e é suficiente.)
- **`#7377A0`** — token de "meta" do tema de newsletter. Dá **4,31:1** sobre branco e
  **reprova AA** para texto pequeno. Descoberto na prova de fogo do modelo de e-mail.
  O `ea-lm-2026` já usa `#576B86` (5,45:1). **Revisar o `ea-radar-news-2026`.**

### Armadilha de contraste registrada
Duas combinações reprovam em WCAG e agora estão sinalizadas no catálogo:
ciano `#00FFEA` como texto sobre branco (1,27:1) e `#2F24FF` como texto sobre navy
(2,60:1). Ciano só sobre fundo escuro; azul primário só sobre fundo claro.

## Próximos passos (para amanhã e diante)

### PRÓXIMO: recorte do catálogo por FRENTES (direção da Criação, 31/07)
A separação combinada é em três eixos + os programas paralelos:
- **Comunicação geral**
- **Comunicação institucional**
- **Comunicação por verticais** (produto)
- **Programas paralelos:** Aulão e-A · Radar Tributário · Jornada do Especialista ·
  Programa de Parcerias · Imersão e-A

A Criação vai passar as orientações. Arquitetura proposta (a confirmar):
**tokens globais** (uma marca só) + **temas por frente** (cada frente com um sotaque —
paleta de acento, grafismo — sobre a mesma base). O catálogo v2 já está preparado para
receber esse eixo: os grupos de navegação são por camada técnica, e o recorte por frente
entra como uma segunda dimensão (filtro/aba), sem reescrever os blocos.

### Direção anterior (mantida): organizar o catálogo por FRENTES
Além das camadas técnicas, o catálogo deve ganhar uma navegação por **frentes/sub-marcas**
que a e-Auditoria aplica — cada uma com sua identidade dentro do sistema:
- **Programa de Parcerias** (identidade própria)
- **Radar Tributário** (a newsletter — já temos os 11 módulos email extraídos)
- **Aulão e-A**
- **Imersão e-A** (evento/webinar — já temos countdown, agenda dia/tarde, speaker, live stream da "Jornada do Especialista", que é o mesmo padrão de evento)
- **O Contador no Comando**
- ...e outras a mapear com a Criação.

> Ideia de arquitetura: **tokens globais** (uma marca só) + **temas por frente** (cada frente
> pode ter um sotaque — paleta de acento, grafismo — sobre a mesma base). Confirmar com a Criação
> quanto cada frente diverge vs. compartilha.

### Expansão do catálogo — ✅ feita na v2
Heros, depoimentos, bento, dataviz fiscal, padrões de evento e os primitivos que faltavam
já estão no catálogo. **Ainda fora:** a **calculadora-isca** (lead magnet fiscal: gate em
2 etapas, `GATE_MODE`, máscara CPF/CNPJ/R$) e o **JourneyStepper** da Jornada — os dois
são padrões grandes o suficiente para merecer entrada própria, não um card de catálogo.

### Higiene do sistema (débitos)
- ~~**Padronizar ícones**~~ ✅ **pago na v2**: o padrão é SVG inline, com set base no catálogo.
- **Normalizar nomenclatura** — aposentar classes `.ea-sN` numéricas e prefixos por projeto (`lc224-`, `je-`, `mx-`) migrando para `ea-<categoria>-<nome>`. **Ainda aberto.**
- **Unificar o navy** — `#050634` é o oficial; `#06063a` só sobrevive em arquivo legado. Regra registrada no catálogo. **Ainda aberto na base instalada.**
- ⚠️ **Débito novo (identificado em 31/07):** o `hero-site` — a peça mais recente e a que
  está no ar na home — usa um **dialeto próprio de tokens** (`--navy`, `--t1`, `--gr-txt`,
  `--f-d`), não `--ea-*`. Ou seja: o DS existe mas ainda não foi **adotado**. Isso não é
  falha do sistema; é o sinal de que falta o passo "como plugar os tokens numa peça nova".

### Validação (o teste de fogo) — ainda não feita
Pegar UMA peça real e reconstruí-la só com blocos do catálogo. Se sair idêntica e mais
rápida, o sistema está provado → escalar. **Melhor cobaia:** o `hero-site`, justamente por
ser o caso do débito acima.

---

## Regras de governança (14 — detalhe no catálogo, seção "Governança")
1. Nunca `&&` no JS do WordPress (o editor recodifica e mata o script inteiro).
2. Escopo por wrapper único; nunca seletor global.
3. **Nenhum `data-*` no wrapper de escopo** — o sanitizador apaga, e leva `class`/`id` junto.
4. **Estado normal não depende de atributo** (`[data-fx="on"]` nunca aplica em produção).
5. **Prefixo também dentro de `@media`** — media query não soma especificidade.
6. **Cor de `<a>` com `!important`** — o tema tem `.inside-article a{color:initial !important}`.
   Corolário: botão sobre fundo escuro não pode depender de texto claro.
7. **Arquivo de entrega sem comentário** — um `*/` órfão engole o bloco seguinte em silêncio.
8. **`@import` na linha 1**, sem nada acima (o editor promove e descarta o que vinha antes).
9. Fail-safe sem JS (conteúdo/números pré-preenchidos). Exceção: player de vídeo.
10. Captura sempre por embed HubSpot (o ID do portal está no gerenciador de senhas da equipe); conferir o `data-form-id`.
11. E-mail é tabela + inline; gradiente sempre com `bgcolor` sólido de fallback.
12. Um CTA amarelo por dobra, texto escuro.
13. **Validar na página publicada**, nunca no preview do editor.
14. **"e-Auditoria" nunca se quebra.**

> Regras 3 a 8 e 13 vieram do diagnóstico de 29/07/2026 documentado em
> `../GUIA-BLOCO-HTML-PERSONALIZADO.md`. Rodar o **Pré-voo** do catálogo antes de colar.
