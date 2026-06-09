\# 📋 ATIVIDADE PRÁTICA — Git \& GitHub

\### Disciplina: Desenvolvimento de Sistemas | SENAI

\---



\## 🎯 Objetivo



Praticar o uso do Git no dia a dia de um desenvolvedor:

criar repositório, fazer commits organizados e documentar o raciocínio pelo histórico.



\---



\## 📁 O Projeto



Você vai trabalhar com o arquivo \*\*`sistema\_escola.py`\*\* — um sistema simples de

gerenciamento escolar com \*\*30 funções em Python\*\*.



O arquivo está funcional, mas contém \*\*7 bugs propositais\*\* espalhados pelo código.

Seu trabalho é encontrá-los, corrigi-los e registrar cada correção com um commit.



\---



\## 📌 Bugs para encontrar e corrigir



| # | Função             | Descrição do bug                                  |

|---|--------------------|---------------------------------------------------|

| 1 | `calcular\_media`   | Divisão usando número fixo `10` em vez de `len()` |

| 2 | `verificar\_aprovacao` | Condição `>= 9` em vez de `>= 6`              |

| 3 | `maior\_numero`     | Comparação `<` em vez de `>`                      |

| 4 | `eh\_palindromo`    | Comparação `!=` em vez de `==`                    |

| 5 | `obter\_nome`       | Chave `"nomes"` em vez de `"nome"`                |

| 6 | `maior\_da\_lista`   | Usando `min()` em vez de `max()`                  |

| 7 | `celsius\_para\_fahrenheit` | Fórmula `\* 5/9` em vez de `\* 9/5`         |

| 8 | `calcular\_troco`   | Subtração invertida                               |



\---



\## 🚀 Passo a Passo



\### Parte 1 — Configuração (faça uma única vez)



```bash

\# 1. Configure seu nome e e-mail no Git

git config --global user.name "Seu Nome"

git config --global user.email "seu@email.com"



\# 2. Crie uma pasta para o projeto

mkdir sistema-escola

cd sistema-escola



\# 3. Inicialize o repositório

git init



\# 4. Copie o arquivo sistema\_escola.py para dentro da pasta



\# 5. Faça o commit inicial

git add sistema\_escola.py

git commit -m "feat: adiciona arquivo inicial do sistema escola"

```



\---



\### Parte 2 — Corrigindo os bugs (1 commit por correção)



Para \*\*cada bug\*\* corrigido, siga este ritual:



```bash

\# 1. Edite o arquivo e corrija o bug

\# 2. Veja o que mudou

git diff sistema\_escola.py



\# 3. Adicione o arquivo

git add sistema\_escola.py



\# 4. Faça o commit com mensagem descritiva

git commit -m "fix: corrige \[descrição do bug] na função \[nome\_função]"

```



\*\*Exemplos de boas mensagens de commit:\*\*

```

fix: corrige calculo de media usando len(notas) na funcao calcular\_media

fix: corrige condicao de aprovacao para media >= 6

fix: corrige formula de celsius para fahrenheit

```



\*\*Exemplos de mensagens RUINS (evite):\*\*

```

arrumei

fix

teste

atualizacao

```



\---



\### Parte 3 — Publicar no GitHub



```bash

\# 1. Crie um repositório público no GitHub com o nome: sistema-escola



\# 2. Conecte seu repositório local ao GitHub

git remote add origin https://github.com/SEU\_USUARIO/sistema-escola.git



\# 3. Envie seus commits

git push -u origin main

```



\---



\### Parte 4 — Verificação final



Após todos os commits, execute o arquivo para verificar se está tudo correto:



```bash

python sistema\_escola.py

```



O resultado esperado deve incluir (entre outros):

```

Média \[7,8,9]: 8.0              ✅

Aprovado com média 6: True      ✅

Maior entre 5 e 3: 5            ✅

É palíndromo 'arara': True      ✅

Celsius 100 → Fahrenheit: 212.0 ✅

Troco R$50 - R$37: 13           ✅

```



\---



\## 📊 Critérios de Avaliação



| Critério                                      | Pontos |

|-----------------------------------------------|--------|

| Repositório criado e publicado no GitHub       | 10 pts |

| Commit inicial com o arquivo original          | 10 pts |

| Bugs corrigidos corretamente (1 pt cada)       | 40 pts |

| Um commit por correção (histórico organizado)  | 20 pts |

| Mensagens de commit descritivas e em português | 20 pts |

| \*\*TOTAL\*\*                                      | \*\*100 pts\*\* |



\---



\## 📤 Entrega



Envie o \*\*link do seu repositório no GitHub\*\* pelo sistema da escola.



Prazo: \_\_\_/\_\_\_/\_\_\_\_\_\_



\---



\## 💡 Dicas



\- Rode o arquivo antes e depois de cada correção para confirmar que funcionou

\- Use `git log --oneline` para ver seu histórico de commits

\- Se errar um commit, não entre em pânico — pergunte ao professor!

\- Cada bug corrigido = 1 commit. Não corrija tudo de uma vez!



\---



\*Boa atividade! Qualquer dúvida, chame o professor.\* 🚀



