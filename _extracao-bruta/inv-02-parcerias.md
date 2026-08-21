# Inventário — HubSpot Parcerias

Arquitetura: template carrega TODO o CSS global em :root + classes; módulos são só HubL + fields.json (módulos "burros"). CSS centralizado no template.

## Módulos (6)
1. ea-hero → Hero com 3 variantes (gradient / minimal / centered). Nav+logo+headline(palavra gradiente)+2 CTA+stats+float_cards+blobs animados. Campo hero_variant.
2. ea-beneficios → TabsFeature: até 4 abas acessíveis (role=tab/tabpanel), cada uma texto+checklist+CTA + vis-card (stat/foto/emoji). JS eaSwTab(). Campos flat tab1..tab4.
3. ea-bento → BentoGrid evento/convidado: grid 4x2, 7 boxes (data, foto convidado, info, apresentadora, tag, stat, cta-mini). Cada box foto opcional+overlay.
4. ea-secao-generica → MediaText 2 colunas: bg light/dark × imagem left/right = 4 combos. Reusável múltiplas vezes.
5. ea-depoimentos → TestimonialCarousel: setas, 3/2/1 cards responsivo, avatar foto ou iniciais fallback. IIFE carrossel.
6. ea-cta-dark → CtaDark: fundo escuro estrelado, float-card glass, headline palavra amarela, btn-glow+btn-ghost, trust note. Âncora #agendar (alvo de todos CTAs).

## Primitivos
- Botões: .btn-p (primário #2F24FF radius50), .btn-o (outline), .btn-glow (glow), .btn-ghost (dark)
- Badges/pills: .pill, .dt-chip "Ao Vivo", .guest-chip, tag retangular. radius 50px ou 8-14px.
- Cards: .pcard, .bc, .vis-card (dots macOS+stat), .testi-card, .s4-float-card (glass). radius 22-28px cards, 40px seções.
- Padrão: .sec-header-center + .sec-title + .sec-sub. Barras progresso .bar/.bar-fill.

## Tokens :root
--cp #2F24FF (primária) · --cb #2488ff · --cl #E4F2FF · --cbg #EFF3FD · --cpur #CE0AFF · --cye #fec008 · --cpk #FF0071 · --cdk #06063a (ATENÇÃO: brand guide usa #050634 — normalizar)
--fd Familjen Grotesk · --fb Manrope · --r 40px. Pílula 50px, cards 24-28, chips 12-16, tags 8.
Padding seção 80/64 → 56/24. Sombras violeta rgba(47,36,255,X). Glassmorphism blur.

## Convenções → regras DS
- Prefixo ea-, kebab, .module. Português.
- CSS no template, módulos só conteúdo.
- Variantes via campo choice + {% if %} + visibilidade condicional no editor.
- Fallback em todo campo de imagem. JS aditivo, sem &&.
- Efeito "encaixe" seções: margin-top -44px, radius 40, z decrescente.
- MELHORIAS: normalizar --cdk; renomear .ea-sN p/ semântico; abas flat→group repetível.
