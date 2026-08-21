# -*- coding: utf-8 -*-
"""
Monta as referencias da skill a partir do llms.txt — que e a fonte da verdade.

Assim nao existem duas copias das regras para sair de sincronia: o llms.txt e escrito
uma vez, e a skill e fatiada dele.
"""
import os
import re
import shutil

from _caminhos import DS, SKILL

SKILL = os.path.join(DS, "skill", "ea-design-system")
REF = os.path.join(SKILL, "references")
SCRIPTS = os.path.join(SKILL, "scripts")

llms = open(os.path.join(DS, "llms.txt"), encoding="utf-8").read()

# fatia o llms.txt por secao numerada
secoes = {}
for m in re.finditer(r"^## (\d+)\.\s+(.+?)$(.*?)(?=^## \d+\.|\Z)", llms, re.M | re.S):
    secoes[int(m.group(1))] = (m.group(2).strip(), m.group(3).strip())

CABECA = ("<!-- Gerado a partir de llms.txt. Não edite aqui: edite o llms.txt e rode "
          "montar_skill.py. -->\n\n")

ARQUIVOS = {
    "regras.md":    ("Regras inegociáveis",       [1, 4, 8]),
    "tokens.md":    ("Tokens: cor, tipo, espaço", [2, 3, 5, 9]),
    "wordpress.md": ("Bloco HTML no WordPress",   [6]),
    "email.md":     ("Peças de e-mail",           [7]),
}

os.makedirs(REF, exist_ok=True)
os.makedirs(SCRIPTS, exist_ok=True)

for nome, (titulo, nums) in ARQUIVOS.items():
    partes = [f"# {titulo}\n"]
    for n in nums:
        if n in secoes:
            partes.append(f"## {secoes[n][0]}\n\n{secoes[n][1]}\n")
    open(os.path.join(REF, nome), "w", encoding="utf-8").write(CABECA + "\n".join(partes))
    print(f"  references/{nome}")

# sub-marcas: escrita a mao, nao esta no llms.txt
SUBMARCAS = CABECA + """# Sub-marcas e programas

Cada uma tem identidade própria **e é autossuficiente** — nunca monte um lockup
`Sub-marca | e-Auditoria`. A assinatura da e-Auditoria só entra junto quando a solicitação
de produção pedir explicitamente.

| Programa | O que caracteriza | Cor própria |
|---|---|---|
| **Imersão e-A** | pílula com **borda em degradê** ciano→azul→violeta, sparkle de 4 pontas, fundo pastel arejado | `#5243FA` |
| **Aulão e-A** | motivo de **player de mídia**: botão de play + pílula, controles de transporte, fundo azul→violeta→magenta | — |
| **Radar Tributário** | ícone de app com sparkline, fundos de bolhas suaves em lavanda e azul | — |
| **O Jogo da Contabilidade** | símbolo em quadrado arredondado + wordmark; território **escuro e cinematográfico** (é programa gravado) | — |
| **Arena Fiscal** | símbolo de Coliseu + wordmark; colorido em degradê ciano→azul→violeta | — |
| **Programa de Parcerias** | selo quadrado "Parceiro Oficial"; 6 versões oficiais em SVG | `#0051FF` |
| **Jornada do Especialista** | tema completo, logotipo em proposta; motivo de turmas manhã/tarde (☀️/🌙) | — |
| **PremIA** | projeto **interno** do time de desenvolvimento. Não vai para cliente. | — |
| **Autores Tributários** | projeto da redação; fundo azul forte, tipografia grande, troféu | — |

## Regras que valem para todas

- O logotipo de cada uma tem versões desenhadas para fundos específicos. Não force uma
  onde a outra é a certa.
- Ao usar SVG oficial de sub-marca **inline**, renomeie as classes: os arquivos exportados
  do Illustrator usam `.cls-1`, `.cls-2` e colidem entre si — o último sobrescreve a cor
  de todos os anteriores, sem aviso. Ou use `<img src="...svg">`.
- A cor própria de um programa **não deve ser normalizada** para o token mais próximo.
  Ela é da identidade dele.
- Mascotes: **e-Bot** é da e-Auditoria (guia de produto, onboarding, tutorial).
  **Incendiária** é da equipe de vendas — campanha interna, ranking, meta.
  Nunca em material de cliente, nunca em peça de compliance.
"""
open(os.path.join(REF, "submarcas.md"), "w", encoding="utf-8").write(SUBMARCAS)
print("  references/submarcas.md")

# o verificador vai junto
shutil.copy2(os.path.join(DS, "ferramentas", "prova-de-fogo.py"),
             os.path.join(SCRIPTS, "prova-de-fogo.py"))
print("  scripts/prova-de-fogo.py")

# tokens.css tambem, para consulta direta
shutil.copy2(os.path.join(DS, "eauditoria-tokens.css"),
             os.path.join(REF, "eauditoria-tokens.css"))
print("  references/eauditoria-tokens.css")

total = sum(os.path.getsize(os.path.join(dp, f))
            for dp, _, fs in os.walk(SKILL) for f in fs)
n = sum(len(fs) for _, _, fs in os.walk(SKILL))
print(f"\nskill montada: {n} arquivos, {total/1024:.1f} KB")
