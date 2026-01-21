# 6. Trabalhando com Funções

#Funções são blocos de código reutilizáveis que realizam uma tarefa específica.

#Exemplo 1:
# Definindo uma função simples
def dsa_saudacao():
    # "Esta função exibe uma saudação simples."
    print("\nOlá! Bem-vindo ao Python.")

# Chamando a função
dsa_saudacao()

#Exemplo 2:
# Definindo uma função que retorna um valor
def dsa_soma_numeros(a, b):
    """Esta função retorna a soma de dois números."""
    return a + b

# Chamando a função e armazenando o resultado em uma variável
resultado = dsa_soma_numeros(5, 3)

# Print
print(f"O resultado da soma é: {resultado}")

#---------------------------------------------------------------------------------------------

## 7. Parâmetros e Argumentos de Funções

#Diferentes formas de passar informações para as funções.

#Exemplo 1:
# Argumentos posicionais
def dsa_apresentacao(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

# Chamando a função
dsa_apresentacao("Ana", 25)

# Chamando a função - CUIDADO!!!
dsa_apresentacao(25, "Ana")

# Argumentos nomeados
dsa_apresentacao(idade = 30, nome = "Bob")

#Exemplo 2:
# Parâmetros com valores padrão (default)
def dsa_saudacao_completa(nome, saudacao = "Olá"):
    print(f"{saudacao}, {nome}!")

# Chamando a função
#dsa_saudacao_completa()

# Chamando a função
dsa_saudacao_completa("Maria")

# Chamando a função
dsa_saudacao_completa("Bob", "Bom dia")

### 7.1. Trabalhando com Número Variado de Argumentos em Funções Python

#Em Python, *args e **kwargs são formas de tornar funções mais flexíveis, permitindo receber um número variável de argumentos sem precisar definí-los todos na assinatura da função.

#*args – argumentos posicionais variáveis

#O asterisco (*) antes do nome indica que a função pode receber qualquer quantidade de argumentos posicionais. Esses valores chegam dentro da função como uma tupla.

#**kwargs – argumentos nomeados variáveis

#Os dois asteriscos (**) indicam que a função pode receber qualquer quantidade de argumentos nomeados (chave e valor). Esses valores chegam dentro da função como um dicionário.

# Argumentos de tamanho variável (*args)
def dsa_soma_numeros(*args):
    
    """Soma um número variável de argumentos."""
    
    total = 0
    
    for numero in args:
        total += numero
    
    return total

print(f"Soma dos Números: {dsa_soma_numeros(1, 2, 3, 4, 5)}")
print(f"Soma dos Números: {dsa_soma_numeros(1, 2, 3)}")
print(f"Soma dos Números: {dsa_soma_numeros(10, 400, 0.3, 120)}")

# Argumentos de tamanho variável (**kwargs)
def dsa_exibe_info_pessoa(**kwargs):
    
    """Exibe informações passadas como pares chave-valor."""
    
    print("\nInformações da Pessoa:\n")
    
    for chave, valor in kwargs.items():
        print(f"- {chave}: {valor}")

dsa_exibe_info_pessoa(nome = "Carla", 
                      profissao = "Engenheira de Dados", 
                      hobby = "Leitura")
dsa_exibe_info_pessoa(nome = "Bob", profissao = "Cientista de Dados")

#---------------------------------------------------------------------------------------------

## 8. Funções Anônimas (Expressão Lambda)

#São pequenas funções anônimas definidas com a palavra-chave lambda.

#Exemplo 1:
# Uma função lambda que dobra um número
dobro = lambda x: x * 2

# Print
print(f"O dobro de 7 é: {dobro(7)}")

#A grande vantagem de usar expressões lambda em Python é a simplicidade e concisão para criar funções pequenas, temporárias e sem nome (anônimas).

#Normalmente, quando você precisa de uma função, define com def. Mas às vezes a função é muito simples e usada apenas uma vez, dentro de outra operação (como um map, filter ou sorted). Nesses casos, a lambda evita código extra e deixa o fluxo mais direto.

#Você pode combinar uma expressão lambda com a função map() para aplicar uma operação a cada elemento da lista, por exemplo.

#Exemplo 2:
# Lista de números
numeros = [1, 2, 3, 4, 5]

# Lambda que retorna o quadrado de cada elemento
quadrados = list(map(lambda x: x ** 2, numeros))

print(quadrados)  # [1, 4, 9, 16, 25]

#Aqui:

#- lambda x: x**2 define uma função anônima que calcula o quadrado.

#- map() aplica essa função a cada elemento da lista.

#- list() converte o resultado do map (um iterador) de volta para lista.

#Também daria para fazer com list comprehension, mas aí não seria lambda.

#Exemplo 3:
# Lista de números
numeros = [1, 2, 3, 4, 5, 6]

# Primeiro calculamos os quadrados com map + lambda
quadrados = list(map(lambda x: x ** 2, numeros))

# Agora filtramos apenas os pares com filter + lambda
quadrados_pares = list(filter(lambda x: x % 2 == 0, quadrados))

print("Quadrados:", quadrados)              # [1, 4, 9, 16, 25, 36]
print("Quadrados pares:", quadrados_pares)  # [4, 16, 36]