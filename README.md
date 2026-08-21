# Design System da e-Auditoria

> ⛔ **Material proprietário — todos os direitos reservados.** Não é material aberto.
> Uso restrito a colaboradores e fornecedores autorizados. Ver [`LICENSE`](LICENSE).

**Concepção, pesquisa, curadoria e construção:** Tamires Fernandes — equipe de Criação da e-Auditoria.
O sistema foi levantado, unificado e documentado por ela a partir de seis landing pages,
trinta e dois módulos de e-mail, o brandbook e o guia técnico.

Banco de elementos oficial da <span>e-Auditoria</span>, controlado pela equipe de Criação.
Marca, sub-marcas, tokens e blocos prontos para landing page (WordPress + HubSpot),
newsletter e peça de rede social.

**Catálogo visual:** [`catalogo.html`](catalogo.html) — 67 seções, 155 blocos com código
para copiar.

---

## Para quem chegou agora

| Você quer… | Vá para |
|---|---|
| Ver os componentes e copiar código | `catalogo.html` |
| Saber o estado do projeto e o que vem a seguir | `00-LEIA-PRIMEIRO.md` |
| Usar os tokens numa peça | `eauditoria-tokens.css` |
| Que o Claude aplique as regras sozinho | `skill/ea-design-system/` |
| Conferir se uma peça fugiu do sistema | `ferramentas/prova-de-fogo.py` |
| Baixar logotipo, mascote ou padrão | `assets/` |
| Publicar isto num domínio | `COMO-PUBLICAR.md` |
| Saber o que falta decidir | `PENDENCIAS.md` |
| Entender o que pode e o que não pode fazer com o material | `LICENSE` |

Se você é um **assistente de IA** lendo este repositório: leia `llms.txt`. Ele tem todas as
regras em texto puro, feito para ser consumido por máquina.

---

## Estrutura

```
catalogo.html              o entregável: catálogo completo, tudo embutido
catalogo-v2.bak.html       a BASE de montagem (não é entregável, mas é fonte)
eauditoria-tokens.css      fonte da verdade dos tokens
llms.txt                   as regras em texto puro, para IA

assets/                    logotipos SVG e PNG, padrões, mascotes, referências
  manifest.json            chave → data URI, consumido pela montagem
fragmentos/                as seções em HTML separado — a FONTE do catálogo
ferramentas/
  prova-de-fogo.py         verificador de conformidade (CLI)
  build/                   os scripts que remontam tudo
skill/ea-design-system/    skill instalável do Claude
registry/                  registry shadcn (tokens)
```

## Como reconstruir o catálogo

O `catalogo.html` é **gerado**, não editado à mão. Ele nasce de
`catalogo-v2.bak.html` (a base com o chrome e os blocos da v2) mais os arquivos de
`fragmentos/`, com as imagens resolvidas a partir de `assets/manifest.json`.

```powershell
python ferramentas/build/montar_pagina_unica.py
```

Para editar uma seção, mexa no arquivo dela em `fragmentos/` e rode o comando de novo.
**Editar o `catalogo.html` direto é perder o trabalho na próxima montagem.**

Os scripts descobrem a raiz do repositório sozinhos (`ferramentas/build/_caminhos.py`),
então funcionam em qualquer máquina sem ajuste. O único caminho externo — a pasta com
as **artes originais**, que não mora no repositório — vem da variável de ambiente
`EA_ACERVO`, e só os scripts de geração de asset precisam dela:

```powershell
$env:EA_ACERVO = "<caminho da pasta e-Auditoria no drive da equipe>"
```

## Antes de entregar qualquer peça

```powershell
python ferramentas/prova-de-fogo.py <arquivo-ou-pasta>
python ferramentas/prova-de-fogo.py <pasta> --email
```

Mede cor (ΔE00 contra a paleta), tipografia, regra do CTA, contraste WCAG, as armadilhas
de produção que já quebraram página no ar, e a grafia da marca. Sai com código 0 se passou.

## As seis regras que não se quebram

1. `e-A` e `e-Auditoria`, nunca `ë-A` — o trema é do desenho do logotipo, não da palavra.
2. Nome sozinho vira logotipo, não palavra escrita.
3. Sub-marca é autossuficiente: não existe `Sub-marca | e-Auditoria`.
4. `e-Auditoria`, `Simples Nacional`, `Simples Híbrido`, `Lucro Real`, `Lucro Presumido` e
   `Reforma Tributária` nunca quebram linha, e vão com inicial maiúscula mesmo sozinhas.
5. CTA é `#FEC008` com texto `#050634`, em pílula. Um por dobra.
6. Assunto da marca-mãe fala em azul e no máximo lilás.

O detalhe de cada uma está no catálogo, seção **Governança** (18 regras).
