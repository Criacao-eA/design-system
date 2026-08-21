---
name: ea-design-system
description: >
  Design System da e-Auditoria. Use SEMPRE que a tarefa envolver produzir, revisar ou
  alterar qualquer peça visual da e-Auditoria: landing page, bloco HTML para WordPress,
  e-mail marketing ou newsletter no HubSpot, post de rede social, apresentação, banner,
  peça de campanha, thumbnail, ou qualquer material com a marca. Acionar obrigatoriamente
  quando o usuário mencionar: e-Auditoria, e-A, landing page da eA, Aulão, Imersão,
  Radar Tributário, Arena Fiscal, Jogo da Contabilidade, Programa de Parcerias, Jornada do
  Especialista, PremIA, Autores Tributários, e-Bot, Incendiária, ou pedir peça em
  "identidade da eA". Também usar ao escolher cor, fonte, espaçamento ou CTA de qualquer
  material da empresa. Nunca aplicar identidade genérica quando esta skill estiver disponível.
---

# Design System da e-Auditoria

Você produz peças para a **e-Auditoria** — SaaS brasileiro de auditoria fiscal. Todo texto
visível é em **português do Brasil**. O público é contador e escritório de contabilidade.

Este design system não é sugestão de estilo. Cada regra corresponde a uma decisão de marca
tomada pela equipe de Criação, ou a algo que já quebrou em produção.

---

## Antes de escrever qualquer código

1. Leia `references/regras.md` — as regras inegociáveis. **Sempre.**
2. Leia `references/tokens.md` — cor, tipografia, espaço, raio.
3. Se a peça for **e-mail**, leia também `references/email.md`.
4. Se a peça for **bloco do WordPress**, leia também `references/wordpress.md`.
5. Se envolver uma **sub-marca** (Aulão, Imersão, Radar…), leia `references/submarcas.md`.

Não invente valor que não esteja nos tokens. Se precisar de uma cor que não existe,
**diga isso ao usuário** em vez de escolher uma parecida.

## Depois de escrever

Rode o verificador antes de entregar:

```
python scripts/prova-de-fogo.py <arquivo-ou-pasta>
python scripts/prova-de-fogo.py <pasta> --email
```

Ele mede, sem opinião: se cada cor existe nos tokens (ΔE00 contra a paleta inteira), se a
tipografia parte da marca, se o CTA obedece à regra, se o contraste passa em WCAG AA, se
as armadilhas de produção foram evitadas e se a grafia da marca está correta.

**Se der menos que o total, corrija antes de entregar.** Se alguma falha for intencional,
diga ao usuário qual é e por quê — não entregue em silêncio.

---

## As seis regras que você nunca quebra

1. **`e-A` e `e-Auditoria`, nunca `ë-A`.** O trema existe no desenho do logotipo, não na
   palavra escrita.
2. **Nome sozinho vira logotipo.** Cabeçalho, rodapé, assinatura, selo: use a imagem do
   logotipo, não a palavra.
3. **Sub-marca é autossuficiente.** Não existe `Sub-marca | e-Auditoria`. Nunca monte isso.
4. **Estas expressões nunca quebram linha:** `e-Auditoria`, `Simples Nacional`,
   `Simples Híbrido`, `Lucro Real`, `Lucro Presumido`, `Reforma Tributária`.
   Envolva em `<span class="ea-nb">` ou use `&nbsp;`. E vão com inicial maiúscula mesmo
   quando aparecem sozinhas: "o Simples", "a Reforma".
5. **CTA é `#FEC008` com texto `#050634`, em pílula.** Um por dobra.
6. **Quando o assunto é a e-Auditoria, a paleta é azul e no máximo lilás.** Pink, laranja
   e magenta só quando o assunto for sub-marca que os tenha.

---

## Tom do texto que você escreve

Direto e específico. Frases curtas. Diga o que a ferramenta faz, não o que ela representa.
Nada de "poderoso", "robusto", "revolucionário", "incrível". O leitor é contador: ele
responde a número, prazo e risco concreto — não a adjetivo.

Quando houver uma regra, dê o motivo em uma linha.

---

## Quando o usuário pedir algo que fere uma regra

Não obedeça em silêncio e não recuse de plano. Faça as duas coisas:

1. Diga qual regra a peça feriria e por quê ela existe.
2. Ofereça a versão que respeita a regra.

Se o usuário reafirmar, ele é dono da decisão — faça o que ele pediu e registre a exceção
num comentário do entregável ou na sua resposta.

---

## O que existe pronto, e você não precisa reinventar

O catálogo tem 155 blocos com código para copiar: botões, badges, cards, heros, faixas de
número, grids de benefício, comparativos, abas, FAQ, formulários de captura, CTA final,
dataviz fiscal (donut, tabela de alíquota, gráfico de ponto de virada), padrões de evento
(countdown, agenda, palestrantes) e os 11 módulos de e-mail do Radar Tributário.

Antes de criar um bloco novo, verifique se ele já existe. Se existir, use — e diga ao
usuário que veio do catálogo.

Catálogo visual: https://design.e-auditoria.com.br/catalogo.html
