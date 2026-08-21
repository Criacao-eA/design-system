<!-- Gerado a partir de llms.txt. Não edite aqui: edite o llms.txt e rode montar_skill.py. -->

# Bloco HTML no WordPress

## REGRAS DE PRODUÇÃO — bloco HTML no WordPress

Cada uma corresponde a algo que já quebrou no ar. Não são estilo.

1. **Zero `&&` no JavaScript.** O editor recodifica o caractere e derruba o script inteiro.
   Use `if` aninhado. Vale até dentro de comentário.
2. **Escopo por wrapper único.** Todo CSS prefixado por uma classe da peça
   (`.ea-home`, `.lp-ptr`). Nunca seletor global.
3. **Nenhum `data-*` no wrapper de escopo.** O sanitizador apaga `data-*` e, nesse
   elemento, leva `class` e `id` junto. Só `class` e `id` sobrevivem.
4. **Nenhuma regra de estado normal dependendo de `[data-*]`.**
5. **Prefixo do wrapper também dentro de `@media`.** Media query não soma especificidade.
   (Esta regra é do WordPress. Em e-mail, classe solta dentro de `@media` é o padrão correto.)
6. **Cor de texto em `<a>` precisa de `!important`.** O tema tem
   `.inside-article a{color:initial !important}`. Corolário: botão sobre fundo escuro não
   pode depender de texto claro — use fundo âmbar com texto navy.
7. **Arquivo de entrega sem comentário.** Um `*/` órfão engole o bloco seguinte em silêncio.
8. **`@import` na linha 1**, nada acima — o editor promove ao topo e descarta o que vinha antes.
9. **Fail-safe sem JS.** Conteúdo e números pré-preenchidos no HTML; o JS só anima.
10. **Captura sempre por embed HubSpot** (portal da e-Auditoria). Nunca form próprio, nunca
    chave de API no front.
11. **Validar na página publicada**, nunca no preview do editor.
