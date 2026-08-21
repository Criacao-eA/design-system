# Como instalar a skill do Design System da e-Auditoria

**Você não precisa saber programar.** São 5 minutos.

> **Se você não entender algum passo:** copie este arquivo inteiro, cole numa conversa com
> o Claude e escreva *"me ajuda a fazer isso, passo a passo"*. Ele foi escrito para que o
> Claude consiga te guiar.

---

## O que é isso, em uma frase

Uma "skill" é um pacote de instruções que o Claude carrega sozinho. Depois de instalada,
sempre que você pedir uma peça da <span>e-Auditoria</span> — landing page, e-mail, post — ele
já vai saber as cores certas, as fontes, as regras da marca e o que não pode fazer.

**Sem a skill:** você precisa explicar tudo toda vez, e ainda assim sai errado.
**Com a skill:** você pede, e sai no padrão.

---

## O arquivo

```
ea-design-system-skill.zip
```

A Criação envia por e-mail ou pelo Teams. **Salve na sua Área de Trabalho** — vai ficar
mais fácil de achar.

⚠️ **Não descompacte ainda.** No Caminho A o arquivo é enviado compactado mesmo.

---

# Caminho A — se você usa o Claude pelo site (claude.ai)

É o caso da maioria. Se você acessa o Claude pelo navegador, é este.

### 1. Abra as configurações

Entre em **claude.ai** e faça login.
No canto **inferior esquerdo**, clique no seu **nome** ou na sua **inicial**.
No menu que abrir, clique em **Configurações** (ou *Settings*).

### 2. Vá em Capacidades

Na coluna da esquerda das configurações, procure **Capacidades** (ou *Capabilities*).
Dentro dela, procure a área de **Skills**.

### 3. Envie o arquivo

Clique em **Fazer upload de skill** (ou *Upload skill*).
Selecione o arquivo `ea-design-system-skill.zip` que você salvou.
Aguarde alguns segundos.

### 4. Confirme que ligou

Deve aparecer na lista uma skill chamada **ea-design-system**.
Verifique se o botãozinho ao lado dela está **ligado**.

**Pronto. Só isso.**

### 5. Teste

Abra uma conversa nova e escreva:

```
Faça um botão de call to action da e-Auditoria em HTML.
```

**Deu certo se** o botão vier com fundo amarelo `#FEC008`, texto azul-escuro `#050634` e
formato de pílula (bem arredondado).

**Não deu certo se** vier um botão azul genérico, ou roxo, ou com texto branco.
Nesse caso, veja "Se não funcionar" no fim deste arquivo.

---

# Caminho B — se você usa o Claude Code (pelo terminal)

Só faça este se você usa o Claude pelo terminal preto do computador. Se não sabe o que é
isso, use o Caminho A.

### 1. Descompacte

Clique com o botão direito no `ea-design-system-skill.zip` → **Extrair tudo**.
Vai aparecer uma pasta chamada `ea-design-system`.

### 2. Copie para a pasta de skills

Abra o **PowerShell** (menu Iniciar → digite `PowerShell`) e cole este comando inteiro:

```powershell
$origem = "$env:USERPROFILE\Desktop\ea-design-system"
$destino = "$env:USERPROFILE\.claude\skills"
New-Item -ItemType Directory -Force $destino | Out-Null
Copy-Item -Recurse -Force $origem $destino
Write-Host "Skill instalada em: $destino\ea-design-system"
```

Se você salvou o arquivo em outro lugar que não a Área de Trabalho, troque o caminho da
primeira linha.

### 3. Reinicie o Claude Code

Feche e abra de novo. A skill é carregada na inicialização.

### 4. Teste

Escreva: `Faça um botão de call to action da e-Auditoria em HTML.`
Deve vir amarelo `#FEC008` com texto `#050634`.

---

# Como usar no dia a dia

Depois de instalada, **você não precisa fazer nada de especial.** É só pedir normalmente:

- "Faça uma landing page para o Aulão e-A sobre correção de SPED"
- "Escreva um e-mail de nutrição para quem baixou o material de Reforma Tributária"
- "Crie um post de Instagram do Radar Tributário"
- "Qual é a cor de CTA da e-Auditoria?"

O Claude carrega as regras sozinho quando percebe que o assunto é da empresa.

### Se ele esquecer

Às vezes, numa conversa muito longa, ele pode não acionar. Escreva:

```
Use a skill ea-design-system.
```

### Uma coisa que ele vai fazer, e é de propósito

Se você pedir algo que contraria uma regra da marca — por exemplo, um CTA azul — ele vai
**avisar antes de fazer**, explicar qual é a regra, e oferecer a versão correta.

Se você confirmar que quer assim mesmo, ele faz. **A decisão é sua.** Ele só não vai
quebrar a regra em silêncio.

---

# Se não funcionar

| O que aconteceu | O que fazer |
|---|---|
| Não achei "Capacidades" nas configurações | Procure por *Capabilities* ou *Skills*. O nome do menu muda conforme o idioma da sua conta. |
| Deu erro ao enviar o `.zip` | Confira se o arquivo não foi renomeado e se tem cerca de 18 KB. Se estiver com 0 KB, o download falhou — peça de novo. |
| A skill aparece mas está desligada | Clique no interruptor ao lado do nome dela. |
| Instalei mas ele continua fazendo botão azul | Abra uma **conversa nova**. A skill não entra em conversas que já estavam abertas. |
| Continua errado numa conversa nova | Escreva `Use a skill ea-design-system.` e repita o pedido. |
| Nada resolve | Chame a equipe de Criação. Não fique tentando — pode ser coisa da conta, não sua. |

---

# O que tem dentro da skill

Só para você saber o que instalou:

| Arquivo | O que é |
|---|---|
| `SKILL.md` | As instruções principais e as seis regras que não se quebram |
| `references/regras.md` | As regras de marca em detalhe |
| `references/tokens.md` | Todas as cores, fontes, espaçamentos e raios |
| `references/wordpress.md` | Regras de bloco HTML no WordPress |
| `references/email.md` | Regras de e-mail |
| `references/submarcas.md` | Aulão, Imersão, Radar, Arena Fiscal, Parcerias e os outros |
| `references/eauditoria-tokens.css` | O arquivo de cores oficial |
| `scripts/prova-de-fogo.py` | Um verificador que confere se a peça saiu no padrão |

Nada disso envia informação para fora. É tudo local, dentro da sua conta.

---

# Para conferir uma peça pronta

Se você recebeu uma peça de um freelancer e quer saber se ela seguiu o padrão, peça ao
Claude:

```
Rode a prova de fogo neste arquivo e me diga o que fugiu do design system.
```

Ele confere seis coisas: se todas as cores existem na paleta, se as fontes são as da marca,
se o CTA está na regra, se o contraste passa nas normas de acessibilidade, se as armadilhas
de produção foram evitadas, e se a grafia da marca está correta.

O resultado vem como uma nota — por exemplo **4/6** — com a lista do que falhou.

---

*Dúvida que este arquivo não resolveu? Fale com a equipe de Criação.*
