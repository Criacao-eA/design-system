<!-- Gerado a partir de llms.txt. Não edite aqui: edite o llms.txt e rode montar_skill.py. -->

# Peças de e-mail

## REGRAS DE E-MAIL

- Layout por `<table>` com estilo **inline**. Nunca flexbox, nunca `var()` (Outlook não entende).
- Larguras: 640px o e-mail, 560px imagem cheia, 436px dentro de card.
- Gradiente sempre com `bgcolor="#..."` sólido de fallback.
- Botão bulletproof: `<td bgcolor>` + `<a>` + `<span style="color:... !important">`.
- Preheader oculto logo após o `<body>`.
- Rodapé com razão social, endereço e `{{ unsubscribe_link }}` com `data-unsubscribe="true"`.
