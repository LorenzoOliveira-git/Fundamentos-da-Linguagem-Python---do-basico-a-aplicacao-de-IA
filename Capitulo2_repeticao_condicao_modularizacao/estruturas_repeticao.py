## 2. Estruturas de Repetição

#As estruturas de repetição (for e while) são usadas para executar um bloco de código várias vezes.

#---------------------------------------------------------------------------------------------

# Loop for

#O loop for é usado para iterar sobre uma sequência (como uma lista, tupla, dicionário, conjunto ou string).

#Exemplo 1:
# Define uma lista
frutas = ["maçã", "banana", "cereja"]

# Imprime a mensagem
print("Frutas disponíveis:")

# Loop pela lista
for fruta in frutas:
    print(f"- {fruta}")

#Exemplo 2:
# Criando uma tupla
cores = ("vermelho", "verde", "azul")

# Loop for percorrendo a tupla
for cor in cores:
    print(cor)

#Exemplo 3:
# Criando um dicionário com o número de cursos em Formações da DSA
formacoes_dsa = {"Formação Cientista de Dados": 6, "Formação Analista de Dados": 4, "Formação Engenheiro de Dados": 5}

# Loop for percorrendo chaves e valores
for chave, valor in formacoes_dsa.items():
    print(chave, ":", valor)

#Exemplo 4:
# Exemplo com a função range()
print("\nContagem até 5:")
for numero in range(6):  # Gera números de 0 a 5
    print(numero)

#---------------------------------------------------------------------------------------------

# Loop while

#O loop while executa um bloco de código enquanto uma condição for verdadeira.

#Exemplo 1:
# Define a variável
contador = 5

# Imprime a mensagem
print("Contagem regressiva:")

# Loop
while contador > 0:
    print(contador)
    contador -= 1

#Exemplo 2:
# Define a variável
contador = 0

# Imprime a mensagem
print("Contagem regressiva:")

# Loop
while contador > 1:
    print(contador)
    contador -= 1

# CUIDADO - LOOP INFINITO - PODE TRAVAR O JUPYTER OU MESMO SUA MÁQUINA
# Define a variável
#contador = 2

# Imprime a mensagem
#print("\nContagem regressiva:")

# Loop
#while contador > 1:
    #print(contador)
    #contador -= 1


#O for em Python é usado quando você já sabe sobre o que quer iterar (como uma lista, tupla, dicionário, string, range, etc.). Ele percorre cada elemento de uma sequência ou iterável de forma automática, sem que você precise gerenciar manualmente a condição de parada.

#Já o while é usado quando você não sabe previamente quantas vezes o loop vai rodar e a repetição depende de uma condição booleana que deve continuar verdadeira para que o loop prossiga. Você precisa cuidar manualmente de alterar o estado dessa condição para evitar loops infinitos.

#Em resumo:

#- for → ideal quando você já tem uma coleção ou um número definido de repetições.

#- while → ideal quando a repetição depende de uma condição que pode mudar dinamicamente ao longo da execução.

#---------------------------------------------------------------------------------------------

# 3. Iteração Sobre Estruturas de Dados com Loops e Condicionais

#Iterar significa percorrer os elementos de uma coleção de dados.

#Exemplo 1 com tuplas:
# Tupla de números
numeros = (3, 7, 10, 15, 20)

# Itera pela tupla e mostra apenas os números pares
for n in numeros:
    if n % 2 == 0:
        print(f"{n} é par")

#Exemplo 2 com listas:
# Lista de nomes
nomes = ["Ana", "Bruno", "Carlos", "Amanda", "Beatriz"]

# Itera pela lista e mostra apenas os nomes que começam com 'A'
for nome in nomes:
    if nome.startswith("A"):
        print(f"Nome encontrado com A: {nome}")

#Exemplo 3 com dicionários:
# Dicionário com produtos e preços
produtos = {"arroz": 25, "feijão": 12, "carne": 45, "macarrão": 8}

# Itera pelo dicionário e mostra apenas produtos acima de 20 reais
for item, preco in produtos.items():
    if preco > 20:
        print(f"{item} custa {preco} reais (acima de 20)")

#---------------------------------------------------------------------------------------------

## 4. Controle de Fluxo em Loops

#As instruções break e continue alteram o fluxo de execução de um loop.

### break

#A instrução break para a execução do loop imediatamente.

#Exemplo 1:
# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Mensagem
print("\nBuscando pelo número 5...")

# Loop com break
for numero in numeros:
    if numero == 5:
        print("Número 5 encontrado!")
        break  # Sai do loop
    print(f"Verificando {numero}...")

# continue

#A instrução continue pula a iteração atual e continua com a próxima.

# Mensagem
print("\nImprimindo apenas os números ímpares:")

# Loop com instrução continue
for numero in range(1, 11):
    if numero % 2 == 0:
        continue  # Pula para a próxima iteração se o número for par
    print(numero)

#---------------------------------------------------------------------------------------------

# 5. Comprehensions (List, Set, Dict e Generator) em Python

#Estas estruturas são consideradas construtores sintáticos (syntactic constructs) ou, mais formalmente, expressões de compreensão (comprehension expressions).

#Na documentação oficial Python, os nomes são:

#- List comprehension → expressão que gera listas.

#- Set comprehension → expressão que gera conjuntos.

#- Dict comprehension → expressão que gera dicionários.

#- Generator expression → expressão que gera iteradores (e pode ser convertido em tupla, lista, etc.).

#Ou seja, o termo técnico mais amplo é comprehension: uma forma mais curta e expressiva de construir coleções (ou geradores) a partir de iteráveis com filtros e transformações aplicadas inline.

#Exemplo 1 usando listas:
# Criando uma lista de quadrados dos números de 0 a 9
quadrados = [x ** 2 for x in range(10)]

# Print
print(f"\nQuadrados de 0 a 9: {quadrados}")

#Exemplo 2 também usando listas:
# Criando uma lista de números pares de 0 a 20
pares = [x for x in range(21) if x % 2 == 0]

# Print
print(f"Números pares de 0 a 20: {pares}")

#Exemplo 3 usando dicionários:
# Cria um dicionário com números e seus quadrados
quadrados_dict = {x: x ** 2 for x in range(6)}
print(quadrados_dict) 

#Exemplo 4 também usando dicionários:
# Conjunto de quadrados (sem valores repetidos)
quadrados_set = {x ** 2 for x in [1, 2, 2, 3, 3, 4]}
print(quadrados_set) 


#Exemplo 5 usando generator para depois transformar em tupla
# Generator expression (não é tupla ainda)
gen = (x ** 2 for x in range(6))
print(gen) 

# Convertendo em tupla
quadrados_tuple = tuple(x ** 2 for x in range(6))
print(quadrados_tuple)  

#Um generator em Python é um iterador especial que não armazena todos os valores na memória de uma vez, mas sim gera cada valor sob demanda. No caso, gen não é uma lista de quadrados de 0 a 5, mas um objeto que sabe como calcular esses valores quando você pedir. A grande vantagem é que o generator economiza memória. 