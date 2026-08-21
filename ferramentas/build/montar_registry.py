# -*- coding: utf-8 -*-
"""
Monta o registry no formato shadcn a partir do eauditoria-tokens.css.

O registry e o formato que permite a um dev rodar
    npx shadcn@latest add https://design.e-auditoria.com.br/r/tokens.json
e receber os tokens dentro do projeto dele.

Comeca pelo que tem valor real e ja existe: os TOKENS. Componente React precisa ser
escrito em React — o catalogo e HTML/CSS, entao esses itens ficam declarados como
pendentes em vez de fingir que existem.
"""
import json
import os
import re

from _caminhos import DS

REG = os.path.join(DS, "registry")
R = os.path.join(REG, "r")           # os .json que o CLI baixa
SRC = os.path.join(REG, "src")       # os arquivos de origem

os.makedirs(R, exist_ok=True)
os.makedirs(SRC, exist_ok=True)

css = open(os.path.join(DS, "eauditoria-tokens.css"), encoding="utf-8").read()

# --- 1. tokens em CSS puro (o que ja existe) --------------------------------
open(os.path.join(SRC, "eauditoria-tokens.css"), "w", encoding="utf-8").write(css)

# --- 2. os mesmos tokens em JSON, para quem consome por JS/Tailwind ---------
pares = re.findall(r"(--ea-[\w-]+)\s*:\s*([^;]+);", css)
tokens = {}
for nome, valor in pares:
    valor = valor.strip()
    if valor.startswith("var("):
        continue
    grupo = "outro"
    if re.match(r"^#|rgba?\(", valor):
        grupo = "cor"
    elif "gradient" in valor:
        grupo = "gradiente"
    elif nome.startswith("--ea-fs") or nome.startswith("--ea-font") or nome.startswith("--ea-lh") or nome.startswith("--ea-tracking"):
        grupo = "tipografia"
    elif nome.startswith("--ea-space") or nome.startswith("--ea-section"):
        grupo = "espaco"
    elif nome.startswith("--ea-radius"):
        grupo = "raio"
    elif nome.startswith("--ea-shadow") or nome.startswith("--ea-glow") or nome.startswith("--ea-blur"):
        grupo = "sombra"
    tokens.setdefault(grupo, {})[nome] = valor
open(os.path.join(SRC, "eauditoria-tokens.json"), "w", encoding="utf-8").write(
    json.dumps(tokens, ensure_ascii=False, indent=2))

# --- 3. itens do registry ---------------------------------------------------
ITENS = [
    {
        "name": "tokens",
        "type": "registry:style",
        "title": "Tokens da e-Auditoria",
        "description": "Cor, tipografia, espaçamento, raio e sombra da marca, como variáveis CSS. É a fonte da verdade — não copie hexadecimal.",
        "files": [
            {"path": "src/eauditoria-tokens.css", "type": "registry:file",
             "target": "styles/eauditoria-tokens.css"},
            {"path": "src/eauditoria-tokens.json", "type": "registry:file",
             "target": "styles/eauditoria-tokens.json"},
        ],
    },
]

registry = {
    "$schema": "https://ui.shadcn.com/schema/registry.json",
    "name": "eauditoria",
    "homepage": "https://design.e-auditoria.com.br",
    "items": ITENS,
}
open(os.path.join(REG, "registry.json"), "w", encoding="utf-8").write(
    json.dumps(registry, ensure_ascii=False, indent=2))

# cada item tambem vira um .json individual em /r, que e o que o CLI busca
for item in ITENS:
    saida = dict(item)
    saida["$schema"] = "https://ui.shadcn.com/schema/registry-item.json"
    arquivos = []
    for f in item["files"]:
        conteudo = open(os.path.join(REG, f["path"]), encoding="utf-8").read()
        arquivos.append({**f, "content": conteudo})
    saida["files"] = arquivos
    open(os.path.join(R, item["name"] + ".json"), "w", encoding="utf-8").write(
        json.dumps(saida, ensure_ascii=False, indent=2))

n_cores = len(tokens.get("cor", {}))
print(f"registry montado")
print(f"  registry.json        {len(ITENS)} item(ns)")
print(f"  r/tokens.json        {round(os.path.getsize(os.path.join(R,'tokens.json'))/1024,1)} KB")
print(f"  tokens extraídos     {sum(len(v) for v in tokens.values())} "
      f"({n_cores} de cor, {len(tokens.get('gradiente',{}))} gradientes)")
print(f"\n  instalação: npx shadcn@latest add https://design.e-auditoria.com.br/r/tokens.json")
