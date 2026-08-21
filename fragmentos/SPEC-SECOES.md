# SPEC — como escrever uma seção do catálogo do Design System e-Auditoria

Você está escrevendo **um fragmento de HTML** que será inserido no arquivo
`design-system/catalogo.html`. Você NÃO edita o catálogo — você grava só o seu fragmento
no caminho de saída que o prompt indicar. Outro processo faz a montagem.

---

## 1. Regras absolutas

- **Idioma: português do Brasil.** Todo texto visível.
- **A palavra "e-Auditoria" NUNCA quebra.** Sempre `<span class="ea-brand">e-Auditoria</span>`.
- **Não use `<!DOCTYPE>`, `<html>`, `<head>`, `<body>`, `<style>` nem `<script>`.**
  Só o markup das seções. CSS novo vai num bloco separado (ver item 4).
- **Nada de imagem externa.** Nenhuma URL `http(s)://` em `src`. Use placeholders (item 3).
- **Escape em blocos de código:** dentro de `<pre>`, todo `<` vira `&lt;`, `>` vira `&gt;`,
  `&` vira `&amp;`. Um `<` cru dentro de `<pre>` quebra a página.
- **Sem emoji como ícone de interface.** Ícone é SVG inline.

## 2. Estrutura obrigatória de cada seção

```html
<section id="ID-KEBAB">
  <div class="sec-head">
    <h2>Título</h2>
    <span class="tag TIPO">Rótulo</span>
    <span class="tag novo">Novo na v3</span>
  </div>
  <p class="sec-desc">Uma ou duas frases sobre o que é e quando usar.</p>

  <div class="comp">
    <div class="comp-head"><h3>Nome do bloco</h3><span class="id">classe-ou-token</span></div>
    <div class="preview stack">  <!-- "stack" = empilhado; sem "stack" = lado a lado -->
      ... preview ao vivo ...
    </div>
    <p class="comp-note">Observação de uso.</p>
    <p class="comp-note warn">Armadilha conhecida / o que quebra.</p>
    <p class="comp-note cro">Nota de conversão, quando fizer sentido.</p>
    <div class="code-wrap"><button class="copy">Copiar</button><pre>CÓDIGO ESCAPADO</pre></div>
  </div>
</section>
```

Classes de `tag` disponíveis: `core` `web` `email` `dataviz` `evento` `cro` `novo`.
Para esta rodada use também `marca` (já existe no CSS de montagem).

Um `.preview` pode ter `class="preview stack dark"` para fundo escuro.

## 3. Imagens — placeholders

Nunca escreva um `src` de verdade. Escreva:

```html
<img src="{{IMG:chave}}" alt="Descrição objetiva" loading="lazy" decoding="async">
```

A montagem troca `{{IMG:chave}}` pelo data URI. **Só use chaves da lista que o seu prompt
fornecer.** Se precisar de uma imagem que não está na lista, não invente — use um
placeholder visual em CSS e diga na `comp-note` que o arquivo está na pasta de origem.

Para SVG que você mesmo autora (padrões, ícones, símbolo), escreva o `<svg>` inline
normalmente — sem placeholder.

## 4. CSS novo

Se a sua seção precisar de CSS que ainda não existe, coloque TODO ele no fim do arquivo,
dentro de um marcador exatamente assim:

```
<!--CSS-INICIO-->
.k-minha-classe{ ... }
<!--CSS-FIM-->
```

Regras para esse CSS:
- Prefixe toda classe nova com `k-` (convenção do catálogo para componentes de preview).
- **Não redefina** nenhuma classe existente: `.comp`, `.preview`, `.sec-head`, `.tag`,
  `.rules`, `.rule`, `.callout`, `.k-btn`, `.k-badge`, `.checklist`, `.code-wrap`, `pre`.
- Use as variáveis do catálogo: `--panel`, `--panel-2`, `--line`, `--ink`, `--ink-soft`,
  `--navy`, `--iris`, `--violet`, `--purple`, `--cyan`, `--yellow`, `--blue`, `--pink`,
  `--r-sm/-md/-lg/-xl/-pill`, `--shadow`, `--ease`, `--font-display`, `--font-body`, `--font-mono`.
- Funciona em tema claro E escuro: cor de texto sempre por `var(--ink)`/`var(--ink-soft)`,
  fundo por `var(--panel)`. Nunca `color:#000` ou `background:#fff` cravados num container.
- Toda animação atrás de `@media (prefers-reduced-motion:no-preference)` ou desligável.

## 5. Botões de download

Padrão do catálogo para baixar um arquivo (a montagem preenche o href):

```html
<a class="k-dl" href="{{IMG:chave}}" download="nome-do-arquivo.png">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"
       stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M4 19h16"/>
  </svg>PNG
</a>
```

Para SVG que você autorou inline, o botão de download é gerado pela montagem a partir de
um `data-svg-src` no container — apenas marque assim:

```html
<div class="k-asset" data-svg-name="ea-simbolo-azul">
  <svg ...>...</svg>
</div>
```

## 6. Tom do texto

Direto, específico, sem marketing. Frases curtas. Diga **quando usar** e **quando não usar**.
Quando houver uma regra, diga o motivo em uma linha. Prefira "não use X porque Y" a
"recomenda-se evitar X". Nada de "poderoso", "robusto", "incrível".

## 7. Fatos da marca que você deve respeitar

- Fontes: **Familjen Grotesk** (display/números, 700, nunca itálico) + **Manrope** (corpo/CTA).
- Azul oficial do **logotipo**: `#2B2E6F`. É diferente do azul primário de **UI** (`#2F24FF`).
  Isso é intencional e precisa ser dito onde for relevante.
- Navy: `#050634`. CTA amarelo: `#FEC008` (texto escuro, nunca branco). Ciano `#00FFEA` só
  como acento sobre fundo escuro.
- Tokens no arquivo `eauditoria-tokens.css`, namespace `--ea-*`.
