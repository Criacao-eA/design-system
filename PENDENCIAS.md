---
projeto: Design System e-Auditoria
atualizado: 2026-08-21
---

# Pendências abertas

O que ficou decidido pela metade e precisa de uma escolha da liderança de Criação.
Cada item traz o problema, a medida e a recomendação — não é lista de tarefa solta.

---

## 1. Decisões de token

### `--ea-purple`: `#8439E6` (tokenizado) vs. `#772BF2` (usado nas artes)

O roxo tokenizado **não apareceu em nenhuma amostragem das artes oficiais**. O que as
verticais realmente usam é `#772BF2`. A diferença é ΔE00 = 3,19 — acima do limiar de
percepção, ou seja, **dá para ver a olho nu**.

**Recomendação:** redefinir `--ea-purple` para `#772BF2` e aposentar `#8439E6`.

> ⚠️ Isso muda em cascata: `--ea-grad-text`, `--ea-grad-text-tri` e `--ea-grad-masthead`.
> Precisa de uma passada de revisão nas peças que usam esses gradientes.

### `#2486FF` vs. `#2488FF`

ΔE00 = 0,71 — abaixo do limiar de percepção. São a mesma cor para o olho humano.

**Recomendação:** normalizar para o token, sem revisão de peça.

### `#7377A0` reprova acessibilidade

Usado no meta do tema de newsletter. Dá **4,31:1** sobre branco e **reprova o AA** em
texto pequeno (o mínimo é 4,5:1). O tema `ea-lm-2026` já usa o correto, `#576B86`.

**Ação:** revisar o `ea-radar-news-2026`. Este não é escolha estética — é conformidade.

### Cores que NÃO devem ser normalizadas

`#0051FF` (Parcerias) e `#5243FA` (Imersão) são cores próprias de sub-marca.
**Mantenha como estão** e registre como token de sub-marca, não como desvio.

---

## 2. Itens de trabalho

- [ ] Subir o tema `ea-lm-2026` no HubSpot.
- [ ] Set de vidro em SVG — ficou em avaliação, aguarda definição.
- [ ] Completar os ativos do Programa de Parcerias no catálogo.
      (Jogo da Contabilidade, Aulão, Radar e Jornada já estão.)

---

## 3. Frente em aberto: chat de consulta ao catálogo

Retomado em agosto/2026. A ideia: um chat que responda dúvidas de marca para pessoas
leigas e fornecedores, apoiado nas contas de IA que a equipe já tem.

Depende de duas coisas que vêm antes:

1. **Controle de acesso definido** (ver `COMO-PUBLICAR.md`) — o chat precisa saber
   quem está perguntando.
2. **Acervo de telas e assets indexado** — as telas do software e as peças do pacote
   Adobe ainda não estão organizadas de forma consultável.
