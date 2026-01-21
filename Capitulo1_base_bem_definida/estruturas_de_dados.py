# 7. Estruturas de Dados - Listas

#Listas são coleções ordenadas e mutáveis de itens. Podem conter diferentes tipos de dados.

# Criando uma lista
frutas = ["maçã", "banana", "laranja", "abacaxi"]
print(f"Lista de frutas: {frutas}")

type(frutas)

# Acessando um item pelo índice
print(f"A primeira fruta é: {frutas[0]}")
print(f"A última fruta é: {frutas[-1]}")

# Adicionando um item ao final da lista
frutas.append("uva")
print(f"Lista após adicionar 'uva': {frutas}")

# Removendo um item
frutas.remove("laranja")
print(f"Lista após remover 'laranja': {frutas}")

# Modificando um item
frutas[0] = "morango"
print(f"Lista após modificar o primeiro item: {frutas}")

# Podemos imprimir diretamente
print(frutas)

# Verificando o tamanho da lista
print(f"A lista tem {len(frutas)} frutas.")

# Deletando a lista
del frutas

# Lista não pode mais ser acessada
# print(frutas)

#---------------------------------------------------------------------------------------------

## 8. Estruturas de Dados - Tuplas

#Tuplas são coleções ordenadas e imutáveis de itens. Uma vez criadas, não podem ser alteradas.

# Criando uma tupla
coordenadas = (10.0, 20.5)
print(f"Tupla de coordenadas: {coordenadas}")

type(coordenadas)

# Acessando um item pelo índice
print(f"Coordenada X: {coordenadas[0]}")
print(f"Coordenada Y: {coordenadas[1]}")

# Tentativa de modificar uma tupla resultará em erro (descomente para ver)
# coordenadas[0] = 15.0

# Tuplas são úteis para dados que não devem ser alterados, como meses do ano, coordenadas, etc.
dias_da_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
print(f"O primeiro dia da semana é: {dias_da_semana[0]}")

#---------------------------------------------------------------------------------------------

# 9. Estruturas de Dados - Dicionários

#Dicionários são coleções de pares chave: valor. São mutáveis.

# Criando um dicionário de informações de um aluno
aluno = {
    "nome": "Bob",
    "idade": 22,
    "curso": "Data Science Para Análise Multivariada",
    "aluno_ativo": True
}

print(f"Dicionário do aluno: {aluno}")

type(aluno)

# Acessando um valor pela sua chave
print(f"Nome do aluno: {aluno['nome']}")
print(f"Curso: {aluno.get('curso')}") # .get() é uma forma segura de acessar chaves

# Adicionando um novo par chave-valor
aluno["cidade"] = "São Paulo"
print(f"Dicionário atualizado:\n {aluno}")

# Modificando um valor existente
aluno["idade"] = 23
print(f"Idade atualizada: {aluno['idade']}")

# Removendo um par chave-valor
del aluno["aluno_ativo"]
print(f"Dicionário após remover a chave 'ativo':\n {aluno}")

#---------------------------------------------------------------------------------------------

## 10. Estruturas de Dados - Conjuntos (Sets)

#Conjuntos são coleções não ordenadas de itens únicos e mutáveis. Eles são úteis para remover duplicatas e realizar operações matemáticas de conjuntos (união, interseção).

# Criando um conjunto (note que os itens duplicados são removidos)
numeros = {1, 2, 3, 4, 2, 3, 5}
print(f"Conjunto de números (sem duplicatas): {numeros}")

type(numeros)

# Adicionando um item
numeros.add(6)
print(f"Após adicionar o valor 6: {numeros}")

# Removendo um item
numeros.remove(2)
print(f"Após remover o 2: {numeros}")

# Operações de conjunto
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

# União (todos os elementos de ambos os conjuntos)
uniao = conjunto_a.union(conjunto_b)
print(f"União de A e B: {uniao}")

# Interseção (elementos que estão em ambos os conjuntos)
intersecao = conjunto_a.intersection(conjunto_b)
print(f"Interseção de A e B: {intersecao}")