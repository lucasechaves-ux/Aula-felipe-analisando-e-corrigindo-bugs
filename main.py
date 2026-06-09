# ============================================================
#  SISTEMA ESCOLAR - Projeto Git | SENAI
#  Disciplina: Desenvolvimento de Sistemas / Git e GitHub
#  Instruções: Cada aluno deve corrigir os bugs indicados,
#              fazer um commit por função corrigida e
#              escrever uma mensagem de commit descritiva.
# ============================================================
#
#  ATIVIDADE:
#  - Existem BUGS propositais em algumas funções (marcadas com # 🐛 BUG)
#  - Corrija cada bug e faça um commit com mensagem clara
#  - Exemplo de mensagem: "fix: corrige calculo de media na funcao calcular_media"
#
# ============================================================


# ------------------------------------------------------------
# BLOCO 1 - OPERAÇÕES MATEMÁTICAS BÁSICAS
# ------------------------------------------------------------

# Função 1 - Soma dois números
def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

# Função 2 - Subtrai dois números
def subtrair(a, b):
    """Retorna a subtração de dois números."""
    return a - b

# Função 3 - Multiplica dois números
def multiplicar(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b

# Função 4 - Divide dois números com proteção contra divisão por zero
def dividir(a, b):
    """Retorna a divisão de dois números. Avisa se b for zero."""
    if b == 0:
        return "Erro: não é possível dividir por zero!"
    return a / b

# Função 5 - Calcula a média de uma lista de notas
    """Recebe uma lista de notas e retorna a média."""
    total = sum(notas)
    qtd = len(notas)
    media = total / qtd  # BUG: deveria dividir por len(notas)
    return media


# ------------------------------------------------------------
# BLOCO 2 - VERIFICAÇÕES E CONDIÇÕES
# ------------------------------------------------------------

# Função 6 - Verifica se um número é par ou ímpar
def par_ou_impar(numero):
    """Retorna 'par' ou 'ímpar' dependendo do número."""
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

# Função 7 - Verifica se o aluno foi aprovado (média >= 6)
    """Retorna True se o aluno foi aprovado (média >= 6)."""
    if media >= 6:  
        return True
    else:
        return False

# Função 8 - Verifica se um número é positivo, negativo ou zero
def classificar_numero(numero):
    """Classifica um número como positivo, negativo ou zero."""
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "zero"

# Função 9 - Verifica se uma senha tem pelo menos 8 caracteres
def senha_valida(senha):
    """Retorna True se a senha tiver 8 ou mais caracteres."""
    if len(senha) >= 8:
        return True
    else:
        return False

# Função 10 - Retorna o maior de dois números
def maior_numero(a, b):
    """Retorna o maior número entre a e b."""
    if a > b:  
        return a
    else:
        return b


# ------------------------------------------------------------
# BLOCO 3 - MANIPULAÇÃO DE STRINGS
# ------------------------------------------------------------

# Função 11 - Transforma o nome em maiúsculas
def nome_em_maiusculo(nome):
    """Retorna o nome todo em letras maiúsculas."""
    return nome.upper()

# Função 12 - Conta quantas letras tem uma palavra (sem contar espaços)
def contar_letras(palavra):
    """Conta o número de letras em uma palavra, ignorando espaços."""
    sem_espacos = palavra.replace(" ", "")
    return len(sem_espacos)

# Função 13 - Inverte um texto
def inverter_texto(texto):
    """Retorna o texto de trás para frente."""
    return texto[::-1]

# Função 14 - Verifica se uma palavra é um palíndromo (ex: "arara")
# 🐛 BUG: a comparação está errada
def eh_palindromo(palavra):
    """Retorna True se a palavra for um palíndromo."""
    palavra = palavra.lower()
    invertida = palavra[::-1]
    if palavra != invertida:  # BUG: deveria ser ==
        return True
    else:
        return False

# Função 15 - Cria um e-mail padrão para o aluno
def criar_email(nome, turma):
    """Gera um e-mail no formato: nome.turma@senai.br"""
    nome_formatado = nome.lower().replace(" ", ".")
    email = f"{nome_formatado}.{turma}@senai.br"
    return email


# ------------------------------------------------------------
# BLOCO 4 - LISTAS E REPETIÇÕES
# ------------------------------------------------------------

# Função 16 - Retorna apenas as notas acima de 5
def notas_aprovadas(lista_notas):
    """Filtra e retorna apenas as notas maiores que 5."""
    aprovadas = []
    for nota in lista_notas:
        if nota > 5:
            aprovadas.append(nota)
    return aprovadas

# Função 17 - Soma todos os números de uma lista
def somar_lista(numeros):
    """Retorna a soma de todos os números de uma lista."""
    total = 0
    for n in numeros:
        total = total + n
    return total

# Função 18 - Retorna o maior valor de uma lista
# 🐛 BUG: está retornando o menor valor, não o maior
def maior_da_lista(numeros):
    """Retorna o maior número de uma lista."""
    return min(numeros)  # BUG: deveria ser max(numeros)

# Função 19 - Conta quantos alunos têm nota maior ou igual a 6
def contar_aprovados(notas):
    """Conta quantos alunos foram aprovados (nota >= 6)."""
    aprovados = 0
    for nota in notas:
        if nota >= 6:
            aprovados += 1
    return aprovados

# Função 20 - Cria uma lista com os quadrados dos números de 1 até n
def lista_quadrados(n):
    """Retorna uma lista com os quadrados de 1 até n."""
    quadrados = []
    for i in range(1, n + 1):
        quadrados.append(i * i)
    return quadrados


# ------------------------------------------------------------
# BLOCO 5 - DICIONÁRIOS (CADASTRO DE ALUNOS)
# ------------------------------------------------------------

# Função 21 - Cria um dicionário com os dados de um aluno
def cadastrar_aluno(nome, idade, turma):
    """Retorna um dicionário com os dados do aluno."""
    aluno = {
        "nome": nome,
        "idade": idade,
        "turma": turma
    }
    return aluno

# Função 22 - Retorna o nome do aluno de um dicionário
# 🐛 BUG: a chave está errada
def obter_nome(aluno):
    """Retorna o nome do aluno a partir do dicionário."""
    return aluno["nomes"]  # BUG: a chave correta é "nome"

# Função 23 - Adiciona uma nota ao cadastro do aluno
def adicionar_nota(aluno, nota):
    """Adiciona o campo 'nota' ao dicionário do aluno."""
    aluno["nota"] = nota
    return aluno

# Função 24 - Verifica se um aluno está cadastrado em uma lista
def aluno_cadastrado(lista_nomes, nome_busca):
    """Retorna True se o nome estiver na lista de alunos."""
    if nome_busca in lista_nomes:
        return True
    return False

# Função 25 - Exibe o boletim do aluno formatado
def exibir_boletim(aluno):
    """Exibe as informações do boletim do aluno."""
    print("===== BOLETIM =====")
    print(f"Nome  : {aluno['nome']}")
    print(f"Turma : {aluno['turma']}")
    print(f"Nota  : {aluno.get('nota', 'Não lançada')}")
    print("===================")


# ------------------------------------------------------------
# BLOCO 6 - FUNÇÕES EXTRAS / DESAFIO
# ------------------------------------------------------------

# Função 26 - Converte temperatura de Celsius para Fahrenheit
# 🐛 BUG: a fórmula está errada
def celsius_para_fahrenheit(celsius):
    """Converte graus Celsius para Fahrenheit. Fórmula: (C * 9/5) + 32"""
    return (celsius * 5 / 9) + 32  # BUG: deveria ser (celsius * 9/5) + 32

# Função 27 - Calcula o IMC de uma pessoa
def calcular_imc(peso, altura):
    """Calcula o IMC: peso / (altura * altura)"""
    imc = peso / (altura ** 2)
    return round(imc, 2)

# Função 28 - Retorna a classificação do IMC
def classificar_imc(imc):
    """Retorna a classificação do IMC em texto."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Função 29 - Calcula o troco de uma compra
# 🐛 BUG: o cálculo do troco está invertido
def calcular_troco(valor_pago, valor_produto):
    """Retorna o troco da compra."""
    troco = valor_produto - valor_pago  # BUG: deveria ser valor_pago - valor_produto
    if troco < 0:
        return "Valor pago insuficiente!"
    return troco

# Função 30 - Gera um relatório final da turma
def relatorio_turma(lista_alunos):
    """
    Recebe uma lista de dicionários com 'nome' e 'nota',
    e exibe um relatório com aprovados e reprovados.
    """
    print("====== RELATÓRIO DA TURMA ======")
    aprovados = 0
    reprovados = 0
    for aluno in lista_alunos:
        status = "✅ Aprovado" if aluno["nota"] >= 6 else "❌ Reprovado"
        print(f"  {aluno['nome']:20s} | Nota: {aluno['nota']} | {status}")
        if aluno["nota"] >= 6:
            aprovados += 1
        else:
            reprovados += 1
    print("--------------------------------")
    print(f"  Total aprovados : {aprovados}")
    print(f"  Total reprovados: {reprovados}")
    print("================================")


# ============================================================
# ÁREA DE TESTES - Rode o arquivo para ver os resultados
# ============================================================

if __name__ == "__main__":

    print("\n--- BLOCO 1: Matemática ---")
    print("Soma 3+5:", somar(3, 5))
    print("Divisão 10/0:", dividir(10, 0))
    print("Média [7,8,9]:", calcular_media([7, 8, 9]))  # BUG: resultado incorreto

    print("\n--- BLOCO 2: Verificações ---")
    print("Par ou ímpar (4):", par_ou_impar(4))
    print("Aprovado com média 6:", verificar_aprovacao(6))   # BUG: retorna False
    print("Maior entre 5 e 3:", maior_numero(5, 3))          # BUG: retorna 3

    print("\n--- BLOCO 3: Strings ---")
    print("Nome maiúsculo:", nome_em_maiusculo("felipe"))
    print("É palíndromo 'arara':", eh_palindromo("arara"))   # BUG: retorna False
    print("Email criado:", criar_email("João Silva", "DS23"))

    print("\n--- BLOCO 4: Listas ---")
    print("Notas aprovadas:", notas_aprovadas([3, 6, 7, 4, 9]))
    print("Maior da lista:", maior_da_lista([3, 6, 7, 4, 9]))  # BUG: retorna 3

    print("\n--- BLOCO 5: Dicionários ---")
    aluno = cadastrar_aluno("Ana", 17, "DS23")
    aluno = adicionar_nota(aluno, 8.5)
    # obter_nome(aluno)  # BUG: vai gerar erro
    exibir_boletim(aluno)

    print("\n--- BLOCO 6: Extras ---")
    print("Celsius 100 → Fahrenheit:", celsius_para_fahrenheit(100))  # BUG
    print("IMC (70kg, 1.75m):", calcular_imc(70, 1.75))
    print("Troco (pago R$50, produto R$37):", calcular_troco(50, 37))  # BUG

    print()
    turma = [
        {"nome": "Ana",     "nota": 8.0},
        {"nome": "Bruno",   "nota": 4.5},
        {"nome": "Carla",   "nota": 7.0},
        {"nome": "Diego",   "nota": 5.9},
        {"nome": "Eduarda", "nota": 9.5},
    ]
    relatorio_turma(turma)
