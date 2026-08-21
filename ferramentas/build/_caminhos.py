# -*- coding: utf-8 -*-
r"""Caminhos do projeto, resolvidos sozinhos.

Nenhum caminho absoluto deve ser escrito nos scripts. Este módulo descobre a
raiz do repositório a partir da própria localização do arquivo, e lê a pasta do
acervo (as artes originais, que moram FORA do repositório) de uma variável de
ambiente.

Uso:

    from _caminhos import DS, ASSETS, MANIFEST, acervo

    origem = acervo("2025", "Auloes", "Imersao eA")

Antes de rodar qualquer script de montagem, aponte o acervo uma vez:

    PowerShell   $env:EA_ACERVO = "C:\caminho\para\a\pasta\e-Auditoria"
    bash         export EA_ACERVO="/caminho/para/a/pasta/e-Auditoria"

Se a variável não estiver definida, os scripts que precisam do acervo avisam com
uma mensagem clara em vez de quebrar com um caminho de outra máquina.
"""
import os

# raiz do repositório: .../design-system  (este arquivo está em ferramentas/build/)
DS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ASSETS = os.path.join(DS, "assets")
MANIFEST = os.path.join(ASSETS, "manifest.json")
MARCA = os.path.join(ASSETS, "marca")
FRAGMENTOS = os.path.join(DS, "fragmentos")
FERRAMENTAS = os.path.join(DS, "ferramentas")
BUILD = os.path.join(FERRAMENTAS, "build")
SKILL = os.path.join(DS, "skill", "ea-design-system")
REGISTRY = os.path.join(DS, "registry")

# pasta de trabalho temporária (saídas intermediárias, nunca versionadas)
SCRATCH = os.environ.get("EA_SCRATCH") or os.path.join(DS, "_tmp")


def acervo(*partes):
    """Caminho dentro do acervo de artes originais (fora do repositório).

    Levanta um erro explicativo se EA_ACERVO não estiver configurada.
    """
    raiz = os.environ.get("EA_ACERVO")
    if not raiz:
        raise RuntimeError(
            "A variável de ambiente EA_ACERVO não está definida.\n"
            "Ela deve apontar para a pasta que contém as artes originais "
            "(a pasta 'e-Auditoria' do drive da equipe).\n\n"
            r'  PowerShell:  $env:EA_ACERVO = "C:\caminho\para\e-Auditoria"' "\n"
            '  bash:        export EA_ACERVO="/caminho/para/e-Auditoria"'
        )
    return os.path.join(raiz, *partes)
