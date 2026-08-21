<!-- Gerado a partir de llms.txt. Não edite aqui: edite o llms.txt e rode montar_skill.py. -->

# Tokens: cor, tipo, espaço

## TIPOGRAFIA

- **Familjen Grotesk** — títulos e números. Peso 700. Nunca itálico. Tracking -0.02em.
- **Manrope** — corpo, CTA, rótulos. Pesos 400 a 600.
- Import: `@import url('https://fonts.googleapis.com/css2?family=Familjen+Grotesk:wght@400;500;600;700&family=Manrope:wght@400;500;600;700&display=swap');`
- Em e-mail, a pilha termina em Arial: `'Manrope','Helvetica Neue',Helvetica,Arial,sans-serif`.

## COR — use apenas estes valores

### Marca
```
#050634  navy / ink / fundo escuro
#2F24FF  íris — primária de UI, botões e links
#4F45F5  violeta
#772BF2  roxo de vertical
#2488FF  azul coringa
#00FFEA  ciano — acento de DADOS sobre fundo escuro, nunca dominante, nunca texto sobre claro
#FEC008  CTA amarelo — cor única de ação
#FB5507  laranja (energia / ao vivo)
#FF0071  pink (expressivo)
#FF2F34  vermelho (alerta)
#2B2E6F  azul do LOGOTIPO — diferente do azul de UI, e isso é intencional
```

### Neutras
```
#FFFFFF branco   #F5F9FC branco gelo   #A2B9DA borda
#576B86 texto secundário   #1E2126 grafite   #E4E9F5 divisor
```

### Pastéis (superfície: "pastel é palco, cor plena é ator")
```
#E7E2FF lilás   #DFE2FF peri   #DBE7FF azul   #EFE6FF lavanda
#FFF0C4 baunilha   #D9F5F0 ciano   #F0E3FF uva   #FFE1F0 rosa
```

### E-mail
```
#E7ECF6 moldura   #F1F2FF card claro   #4A4D6B corpo
#576B86 texto secundário (NÃO use #7377A0: dá 4,31:1 sobre branco e reprova AA)
```

### Cor de sub-marca
```
#0051FF Programa de Parcerias   #5243FA Imersão e-A
```

### Paletas por vertical (a proporção é a de uso)
```
Integrar ................ #772BF2 66% · #4F45F5 34%
Atualizar regras fiscais  #00FFEA 39% · #2486FF 39% · #2F24FF 21%
Auditar arquivos ........ #2F24FF 39% · #2486FF 39% · #050634 21%
Recuperar crédito ....... #2486FF 39% · #2F24FF 39% · #00FFEA 21%
Reforma Tributária ...... #2486FF 40% · #772BF2 22% · #4F45F5 19% · #00FFEA 19%
Corrigir SPED ........... #772BF2 40% · #2486FF 39% · #4F45F5 21%
```

## GEOMETRIA E ESPAÇO

```
raio:    12px chip · 20px card · 28px card grande · 40px seção · 100px/999px pílula
espaço:  escala de 8px — 4 8 12 16 24 32 48 64 96
seção:   padding-block: clamp(4rem, 9vw, 7.5rem)
container: 1180px
```

## ÍCONES

SVG inline, 24×24, `stroke-width:1.75`, `stroke-linecap/linejoin: round`, `fill:none`,
cor por `currentColor`. Decorativo leva `aria-hidden="true"`. Dentro de botão, largura e
altura explícitas (16px) — se o CSS de escopo cair, o SVG não incha.

Ícone 3D é para destaque, hero e social. Nunca em UI funcional, nunca misturado com o set
2D na mesma grade, nunca abaixo de 48px.
