# Inventário — Nova News (Email/Newsletter "Radar Tributário")

Email-safe: tabelas, inline styles, bgcolor, larguras fixas 640/560/436px, botões em <td>. HubL. Template email-radar-news.html = shell 640px card radius24, empilha 11 módulos. CSS inline nos módulos; <style> do template só guarda media queries + prefers-color-scheme dark ([data-ogsc] p/ Outlook.com).

## Módulos (11) — ordem canônica: cabecalho→midia→hero→prazo→artigo→banner→card→caso→enquete→evento→footer
1. ea-news-cabecalho → header/masthead: logo eA + "ver no navegador" + masthead gradiente 122deg #8439E6→#5B4BF2→#2488FF (fallback #4F45F5) + selo pill.
2. ea-news-midia → slot imagem full opcional (só renderiza se src). 560px radius16 + legenda.
3. ea-news-hero → título edição 2 pesos (forte #050634 + suave #8A93B8) + eyebrow + subtítulo.
4. ea-news-prazo → ÂNCORA NAVY (KPI herói): card #050634 radius20, tag pill ciano, número gigante 64px, sweep ciano 48x3, divisor, linha fato 2 col (stack no mobile).
5. ea-news-artigo → lista editorial repetível artigos[]: pill de IMPACTO (alto/medio/operacional/nenhum) + categoria + título + resumo + link seta. Divisor entre itens.
6. ea-news-banner → banner full opcional (idêntico midia, padding topo 40, sem legenda). CRO: depois do editorial.
7. ea-news-card → novidade plataforma: card claro #F1F2FF radius20, imagem 436, rótulo, título, texto, botão bulletproof #2F24FF.
8. ea-news-caso → caso de sucesso: card #F7F9FD, pill violeta + nome cliente, botão ghost #E7E9FF.
9. ea-news-enquete → enquete: cada opção é LINK rastreável (email não roda form). opcoes[] células #F7F9FD borda radius12.
10. ea-news-evento → card navy evento ao vivo: badge "AO VIVO" gradiente laranja→vermelho (#FB5507→#FF2F34, fallback sólido), data/hora, apresentadores, CTA #2F24FF.
11. ea-news-footer → compliance: logo, razão social, endereço, {{unsubscribe_link}} data-unsubscribe="true" + {{subscription_preferences_url}}.

## Primitivos email-safe
- Botão bulletproof: <td bgcolor="#2F24FF" radius100 mso-padding-alt> <a> <span color:#FFFFFF !important>. Ghost: bgcolor #E7E9FF ou branco+borda.
- Pill/badge: <td bgcolor radius100 uppercase letter-spacing>. 
- Divisor hairline: <td height=1 bgcolor style height/line-height/font-size 1px>.
- Sweep acento: <td width48 height3 bgcolor #00FFEA>.
- Spacer vertical: <td height N line-height N font-size N>.
- Imagem fluida: width 560/436 style width100% height auto max-width display block radius14-16.
- Card container: table bgcolor radius18-20 + td card-pad 30-34.
- Preheader oculto: display none max-height0 mso-hide all.
- Stack responsivo: .stack display block width100%.

## Tokens
Navy #050634 · violeta CTA #2F24FF · secundários #4F45F5 #5B2BD9 #8439E6 #2488FF · ciano #00FFEA (só no navy) · AO VIVO #FB5507→#FF2F34.
Superfícies: moldura #E7ECF6, cartão branco, cards claros #F1F2FF/#F7F9FD, rodapé #F5F8FC, botão sec #E7E9FF.
Texto: corpo #4A4D6B, meta #7377A0/#8A93B8/#9AA3D6/#AEB4CE.
IMPACTO: alto bg#FFE7E7/txt#C7202B🔴 · médio #FFF3D1/#9A6A00🟡 · operacional #E2EEFF/#1667D6🔵.
Divisores #E4E9F5 / #EDF0F8 / navy #1D1F53.
Tipografia: Familjen Grotesk 700 + Manrope 400-800, pilha completa (nunca só Arial). h1 34/39(27mob), sec-h2 22, card-h 22, art-h 19, âncora 64(48mob), corpo 14-15, meta 11-13.
Raios: cartão 24, cards 18-20, imagens 14-16, enquete 12, pills/botões 100.
Larguras: email 640, full 560, dentro card 436, padding lateral 40 (20-22 mobile).

## Evolução v1→v3
v1: conteúdo-primeiro, NÃO email-safe (classes, emoji literal, rgba), KPI strip 3 col.
v2: vira email-safe (tabelas, bgcolor, sem rgba/emoji), cria âncora navy + medidor de barras, cartão fica claro no dark.
v3: identidade Radar completa (masthead gradiente, logos), volta pills coloridas com emoji + legenda de código, slots mídia opcionais. É a base dos 11 módulos.
