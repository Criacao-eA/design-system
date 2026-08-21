---
projeto: Design System e-Auditoria
atualizado: 2026-08-21
---

# Como publicar o Design System

Três destinos, três públicos. Não são alternativas — são camadas.

| Destino | Para quem | O que resolve |
|---|---|---|
| **Site com acesso controlado** | Criação, Marketing, fornecedores | ver, copiar e baixar |
| **Skill do Claude** | quem tem conta Claude | o assistente **aplica** as regras sozinho |
| **Registry** | time de desenvolvimento | os tokens entram no produto |

---

## ⚠️ Antes de tudo: este material é proprietário

O catálogo reúne logotipos, sub-marcas, mascotes e peças de campanha da
<span>e-Auditoria</span>. **Não é material aberto.** Uma decisão anterior deste projeto
dizia que "público é aceitável porque não há nada confidencial" — essa avaliação foi
**revista e está errada**: o risco não é vazamento de segredo, é **reprodução da marca
por terceiros** e cópia do sistema por outros times de design.

Regras que valem para qualquer forma de publicação:

1. O repositório é **privado**. Sempre.
2. O site fica **atrás de autenticação**, mesmo para consulta.
3. Fornecedor recebe acesso **nominal** e temporário — que é revogado no fim do contrato.
4. Arte-master (vetor editável, arquivo do pacote Adobe, mascote em alta) **não vai para
   o repositório**. É entregue sob solicitação.

---

## 1. O site — repositório privado + Cloudflare Pages

O GitHub Pages gratuito **só funciona em repositório público**, e público significa
clonável por qualquer pessoa. Por isso a hospedagem não fica no GitHub.

O Cloudflare Pages publica direto de um repositório **privado**, de graça, e o
Cloudflare Access coloca uma porta com fechadura na frente — também de graça,
para até 50 pessoas.

### Passo a passo

1. **Deixar o repositório privado**
   `Settings → General → Danger Zone → Change repository visibility → Private`

2. **Criar o projeto no Cloudflare**
   `Workers & Pages → Create → Pages → Connect to Git` → autorizar o GitHub e escolher
   o repositório `design-system`.

3. **Configuração de build**
   Não há build: é HTML estático.
   - Framework preset: `None`
   - Build command: *(vazio)*
   - Output directory: `/`

4. **Ligar o Access** *(este é o passo que protege — não pule)*
   `Zero Trust → Access → Applications → Add an application → Self-hosted`
   - Aponte para o domínio do projeto.
   - Em **Policies**, crie duas:
     - **Equipe** — regra `Emails ending in` → `@e-auditoria.com.br`
     - **Fornecedores** — regra `Emails` → lista nominal, um a um.
   - Método de login: **One-time PIN**. A pessoa recebe um código por e-mail e entra.
     Não precisa criar conta em lugar nenhum.

5. **Domínio próprio** *(opcional)*
   `Custom domains → Set up a domain` → `design.e-auditoria.com.br`.
   Peça ao TI o registro CNAME.

### Para atualizar

```powershell
git add .
git commit -m "o que mudou"
git push
```

O Cloudflare republica sozinho em cerca de um minuto, e fica o histórico de quem
mudou o quê.

### Revogar um acesso

`Zero Trust → Access → Applications → Policies` → tire o e-mail da lista.
Vale na hora, sem precisar trocar senha de ninguém.

---

## 2. A skill do Claude — o que faz a regra ser aplicada

Hospedar torna **disponível**. A skill torna **aplicado**. É a diferença entre alguém
poder consultar e o assistente já saber.

A pasta `skill/ea-design-system/` está pronta. Cada pessoa instala uma vez —
o passo a passo para pessoa leiga está em `COMO-INSTALAR-A-SKILL.md`.

### Como a skill se mantém em sincronia

As referências são **geradas a partir do `llms.txt`**, que é a fonte única. Se uma regra
mudar, edite o `llms.txt` e rode `ferramentas/build/montar_skill.py`. Nunca edite
`skill/ea-design-system/references/*.md` na mão: elas têm um aviso no topo por isso.

> **Cuidado ao distribuir o `.zip`:** ele carrega as regras da marca. Envie por canal
> interno (Teams, e-mail corporativo), nunca por link público.

---

## 3. Registry — para o time de desenvolvimento

`registry/r/tokens.json` está montado com os **84 tokens** extraídos do
`eauditoria-tokens.css` (32 cores, 9 gradientes, tipografia, espaço, raio e sombra).

> ⚠️ **O registry pressupõe endereço acessível sem login.** Com o Access ligado, o
> `npx shadcn add` não consegue baixar. Se o time de produto for consumir os tokens,
> a saída é publicar **só o `registry/`** num endereço aberto — são valores de cor e
> espaçamento, sem logotipo e sem arte, e isso não cria risco de clonagem da marca.
> Decida isso quando houver demanda real; não precisa resolver agora.

O registry também aceita componentes, mas o catálogo é HTML/CSS/HubL e o shadcn espera
React. Escrever esses componentes é **decisão do time de produto**, não da Criação.
A sequência saudável: publicar os tokens → o time usa → se pedirem componentes, escolhem
os 5 ou 6 mais usados. Fazer o último passo primeiro é escrever componente que ninguém pediu.

---

## 4. Como o fornecedor usa

Da forma mais confiável para a mais frágil:

1. **Instala a skill.** O Claude dele passa a aplicar as regras sozinho. Melhor caminho
   para quem é leigo, porque não depende de disciplina.
2. **Recebe o `llms.txt`.** São 15 KB de texto puro, que o assistente lê inteiro.
   Melhor que mandar o catálogo, que é grande e vai ser truncado.
3. **Consulta o catálogo visual.** Bom para pessoa, ruim para máquina.

**E em qualquer um dos três casos, a entrega passa pelo verificador:**

```powershell
python ferramentas/prova-de-fogo.py peca.html
python ferramentas/prova-de-fogo.py pasta-do-tema/ --email
```

É o que transforma "confio que seguiu" em "verifiquei que seguiu". Funciona mesmo com
quem nunca leu o catálogo, e é o único item da lista que não depende de boa vontade.

---

## Ordem recomendada

1. Deixar o repositório privado.
2. Publicar no Cloudflare Pages e **ligar o Access** antes de divulgar o endereço.
3. Instalar a skill nas contas do time e testar numa peça real.
4. Registry: só quando o time de produto pedir.
