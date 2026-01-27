## 4. Indexação e Fatiamento

#Acessar e modificar subconjuntos de dados em arrays é simples e poderoso.

import numpy as np

# Vamos criar uma matriz 4x4 com números de 0 a 15
dados = np.arange(16).reshape(4, 4)
print("\nMatriz Original:\n")
print(dados)

# Acessando um elemento específico: linha 1, coluna 2 (lembre-se que a indexação em Python começa em 0)

print("\nMatriz Original:\n")

print(dados)

elemento = dados[1, 2]

print(f"\nElemento na posição [1, 2]: {elemento}\n")

# Fatiando para obter a primeira linha completa (sintaxe pelo índice da linha)

print("\nMatriz Original:\n")

print(dados)

primeira_linha = dados[0] 

print(f"\nPrimeira linha:\n{primeira_linha}\n")

# Fatiando para obter a primeira linha completa (sintaxe pelo índice da linha e da coluna). RECOMENDADO.

print("\nMatriz Original:\n")

print(dados)

primeira_linha = dados[0, :]

print(f"\nPrimeira linha:\n{primeira_linha}\n")

# Fatiando para obter a segunda coluna completa

print("\nMatriz Original:\n")

print(dados)

segunda_coluna = dados[:, 1]

print(f"\nSegunda coluna:\n{segunda_coluna}\n")

# Fatiando um bloco 2x2 do canto superior esquerdo

print("\nMatriz Original:\n")

print(dados)

bloco_superior_esquerdo = dados[:2, :2]

print(f"\nBloco 2x2 superior esquerdo:\n{bloco_superior_esquerdo}\n")

# Indexação booleana: selecionando apenas os números maiores que 10

print("\nMatriz Original:\n")

print(dados)

maiores_que_10 = dados[dados > 10]

print(f"\nNúmeros maiores que 10:\n {maiores_que_10}")

# Cria a matriz
matriz = np.arange(25).reshape(5, 5)

# Usamos o passo no slicing (start:stop:step)
# Para as linhas: '::2' significa do início ao fim, pulando de 2 em 2 (0, 2, 4)
# Para as colunas: '1::2' significa do índice 1 ao fim, pulando de 2 em 2 (1, 3)

resultado = matriz[::2, 1::2]

print("Matriz Original:")
print(matriz)
print("\nLinhas Pares e Colunas Ímpares:")
print(resultado)