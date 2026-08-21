# Inventário — Jornada do Especialista (HubSpot, evento/webinar)

Template lp-jornada.html hospeda CSS+JS, 15 módulos ea-jor-*. Wrapper .je-lp mx-lp. 3 namespaces: je-* (core), jh-* (4 variantes hero), mx-* (seções ricas extras). entrega-tema/ = protótipos 1:1.

## Módulos (15)
1. ea-jor-hero → EventHero, 4 variantes (bento / fotos-no-título / orbitando / dados-ao-redor) × claro/escuro. Nav sticky, infocard, turma cards.
2. ea-jor-countdown → ⭐ CountdownBar: data-target ISO, 4 boxes dias/horas/min/seg, tema sunrise→dusk, setInterval 1s.
3. ea-jor-transmissao → ⭐ LiveStream: iframe YouTube embed + live_chat 2 colunas, empty state.
4. ea-jor-programacao → ⭐ AgendaSchedule: parts numeradas repetíveis + 2 TurmaCard dia(☀️ warm)/tarde(🌙 purple+estrelas). Motivo mais reusado.
5. ea-jor-palestrantes → ⭐ SpeakerGrid: card retrato 3:4, badge, bio hover-reveal, scrim.
6. ea-jor-depoimentos → TestimonialCarousel: 3/2/1 responsivo, aspas gigante, avatar/iniciais.
7. ea-jor-porque → BenefitCardGrid: cards pastel inclinados, emoji tag chip.
8. ea-jor-generica → MediaText 50/50, image left/right, claro/escuro.
9. ea-jor-palavras → WordCloudScatter interativo: pills espalhadas convergem no scroll.
10. ea-jor-levar → TakeawaysBento: bento assimétrico, cards gradiente numerados.
11. ea-jor-numeros → StatsPanel (mx, default DARK): números grandes acento ciano, glass cards.
12. ea-jor-grupos → CommunityMarquee: marquee infinito auto-scroll, pausa hover.
13. ea-jor-destaques → FeatureList/SpotlightRows (default DARK): linhas logo+org+meta+tags, confetti.
14. ea-jor-jornada → ⭐ JourneyStepper (default DARK, jogo): 5 passos, % sucesso, botão avançar, confetti, parallax mouse.
15. ea-jor-final → FinalCTA: badge escassez (vagas), 2 CTAs.

## Primitivos
- Botões: .je-btn-p (amarelo #fec008 ink radius50 glow), .je-btn-o (outline branco/violeta), .je-btn-ghost.
- .je-kicker chip, .je-infocard, .je-hl (highlight pill rotacionado gradiente), .je-grad (texto), .je-head (cabeçalho seção).
- .je-panel+.je-tuck (radius40, margin negativo = seções encaixam como cartões).
- .je-reveal+.in +d1-d6 (IntersectionObserver fade-up escalonado).
- TurmaCard dia/tarde (☀️/🌙) — motivo mais reusado, aparece em hero e programação.
- [data-count] counter rAF. .je-ph placeholder listrado. .je-orbit/.jhB-card chip flutuante.
- .no-js/.je-edit fail-safe (reveal off no editor/sem JS).

## Tokens :root (.je-lp)
--blue #2488ff --iris #2f24ff --violet #4f45f5 --purple #8439e6 --cyan #00ffea --yellow #fec008 --pink #ff0071 --ink #050634 --ink2 #576b86. page bg #F1EAFF, text #231f45.
Pastéis: --p-lilas #E7E2FF --p-peri #DFE2FF --p-azul #DBE7FF --p-lav #EFE6FF --p-baun #FFF0C4 --p-ciano #D9F5F0 --p-uva #F0E3FF --p-rosa #FFE1F0.
--fd Familjen Grotesk (700, -.02em) --fb Manrope (400-800). @import Google Fonts.
--r 40px. cards 20-28, pills/botões 50. Sombra violeta rgba(60,40,140,.10-.18). Glow botão rgba(254,192,8,.36).
H1 clamp40-76, H2 clamp28-58, sub 15-19. Motion float5-6s/twinkle3s/marquee34s/confetti, gated prefers-reduced-motion.

## Theme model
Light-dominant + bg_style claro/escuro POR SEÇÃO em cada módulo. je-* default claro; mx-* (números/destaques/jornada) default ESCURO.

## Padrões de EVENTO de maior valor: CountdownBar, AgendaSchedule+TurmaCard dia/tarde, LiveStream, SpeakerGrid, JourneyStepper.
