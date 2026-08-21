# assets/ — arquivos da marca

Gerado em 31/07/2026 a partir de
`2025/Nova IDV/Brandbook/Apresentação/Links`. Esta pasta é **derivada**: a origem
continua sendo o brandbook. Se um logotipo mudar lá, regere aqui.

## O que tem aqui

| Pasta | Conteúdo |
|---|---|
| `marca/` | Logotipos: **SVG vetorial** + PNG de alta em 3 cores e 3 tamanhos |
| `padroes/` | Padrões de fundo tileáveis em SVG (~600 bytes cada) |
| `mascotes/` | e-Bot e Incendiária, WebP otimizado |
| `vidro/`, `icones/`, `backgrounds/` | Referências visuais, WebP otimizado |
| `manifest.json` | Chave → data URI. É o que a montagem do catálogo consome |

## O vetor não existia antes

Os arquivos oficiais do logotipo eram **PNG pequeno**: o horizontal tinha 641×75 px
e o vertical 139×148 px. Não dá para ampliar raster sem perder — então "PNG em alta
resolução" simplesmente não existia.

Os `.svg` desta pasta foram obtidos por **vetorização dos PNGs** (marching squares
subpixel + Douglas-Peucker, com `fill-rule="evenodd"` para vazar as contra-formas).

A fidelidade foi medida **duas vezes, por métodos independentes**, e os números não
batem — vale entender por quê antes de citar qualquer um deles:

| Arquivo | Na resolução nativa | Reamostrado a 600px |
|---|---|---|
| `ea-simbolo.svg` | 0,131% | 0,34% |
| `ea-horizontal.svg` | 0,187% | 2,76% |
| `ea-vertical.svg` | 0,248% | 1,65% |
| `arena-fiscal.svg` | 0,095% | 2,13% |
| `imersao-ea.svg` | 0,120% | — |

A primeira coluna compara na resolução original, sem reamostrar. A segunda reduz os dois
lados para 600px e recorta o original pela caixa de conteúdo — o que **soma erro de
reamostragem e de alinhamento de caixa** ao erro de forma. A prova de que a diferença é
essa, e não forma errada: na imagem de diferença o que aparece é um **fio de contorno**,
não manchas. Erro de forma real produziria blocos.

Ou seja: a fidelidade de forma é a da primeira coluna; a segunda é um teto pessimista.
Qualquer uma das duas está confortavelmente dentro do aceitável para logotipo.

**Ressalvas honestas do método:**
- Vetorização é reconstrução, não o arquivo original. Para impresso de alta exigência
  (offset, sinalização grande), peça o `.ai`/`.eps` ao estúdio que fechou a marca.
- Os paths são **polilinha, sem Bézier** — em zoom extremo aparece facetamento.
- O `imersao-ea.svg` não usa a silhueta do alfa (que seria só a pílula cheia): usa
  `alfa × (255 − min RGB)`, o que produz a pílula com o **texto vazado**. É o
  comportamento certo para uma versão monocromática, mas significa que ele não é
  comparável com a máscara alfa do PNG — daí o "20% de divergência" que uma medição
  ingênua acusa. O sparkle ficou aproximado.
- O `viewBox` é justo à geometria, não à caixa do PNG. Isso muda o respiro embutido:
  ao trocar um PNG antigo por estes SVGs num layout, confira o espaçamento.

## PNG de alta

Já gerados em `marca/`, nas cores **azul** (`#2B2E6F`), **preto** (`#050634`) e
**branco**, nas larguras 1000/2000/4000 px (horizontal), 600/1200/2400 (vertical) e
512/1024/2048 (símbolo).

No catálogo publicado não é preciso baixar daqui: o botão **PNG** gera o arquivo na hora,
a partir do vetor, em canvas. Qualquer largura, qualquer cor, sem peso na página.

## Cores da marca — atenção

O azul do **logotipo** é `#2B2E6F`. O azul primário de **UI** é `#2F24FF`. São cores
diferentes e isso é intencional: não normalize uma pela outra.

## Como regerar

Os scripts ficam no scratchpad da sessão que os produziu. O fluxo é:
`build_assets.py` (otimiza + manifest) → vetorização → `gerar_altares.py` (PNG de alta a
partir do SVG) → `montar_catalogo.py` (injeta no catálogo). Se precisar rodar de novo e os
scripts não estiverem mais lá, o caminho está descrito em `../00-LEIA-PRIMEIRO.md`.
