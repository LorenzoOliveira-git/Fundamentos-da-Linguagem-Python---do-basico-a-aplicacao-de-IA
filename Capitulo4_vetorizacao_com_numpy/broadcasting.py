## 7. Broadcasting e Operações Entre Arrays

#No NumPy, broadcasting é o mecanismo que permite realizar operações aritméticas entre arrays de formas (shapes) diferentes, sem precisar copiar ou replicar manualmente os dados. 

#Ele funciona expandindo automaticamente as dimensões de arrays menores para que fiquem compatíveis com os maiores, seguindo um conjunto de regras. Isso evita laços (loops) explícitos e melhora muito a eficiência. 

#Por exemplo, se você soma uma matriz 3×3 com um vetor de 3 elementos, o NumPy “estica” o vetor para que cada linha da matriz receba a soma correspondente elemento a elemento, sem criar cópias extras na memória.

import numpy as np 

# Matriz 3x3
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
type(matriz)

matriz.shape

# Vetor 1D com 3 elementos
vetor = np.array([10, 20, 30])
type(vetor)
vetor.shape

#Queremos somar os valores do vetor aos valores de CADA linha da matriz.

print(matriz)
print(vetor)

# Broadcasting: o vetor é "expandido" para cada linha da matriz
resultado = matriz + vetor

print("\nMatriz original:\n", matriz)
print("\nVetor:\n", vetor)
print("\nResultado com broadcasting:\n", resultado)

# Matriz com faturamento de 3 produtos em 4 meses
faturamento = np.array([
    [100, 110, 120, 130], # Produto A
    [200, 210, 220, 230], # Produto B
    [300, 310, 320, 330]  # Produto C
])
type(faturamento)
# Shape
faturamento.shape

# Vetor com um bônus (incentivo) para cada produto
bonus_por_produto = np.array([5, 10, 15])
type(bonus_por_produto)
# Shape
bonus_por_produto.shape

#Queremos adicionar um bônus a cada valor de faturamento, por linha. Ou seja, todos os itens da primeira linha devem receber o bônus de 5, por exemplo, e assim por diante.

print("\nFaturamento:\n")
print(faturamento)
print("\nBônus por Produto:\n")
print(bonus_por_produto)

# Poderíamos usar a vetorização e fazer algo assim:

#faturamento_com_bonus = faturamento + bonus_por_produto

#Mas, por que a mensagem de erro? A própria mensagem já explica o que está ocorrendo.

# O NumPy "estica" (broadcast) o vetor bônus para que ele possa ser somado à matriz
# Mas forma de `bonus_por_produto` (3,) é incompatível com (3, 4)
# Para somar, precisamos que tenha a forma (3, 1) para o broadcast funcionar nas colunas
bonus_formatado = bonus_por_produto.reshape(3, 1)

bonus_formatado.shape

print("\nBônus por Produto:\n")
print(bonus_formatado)

# Agora sim
faturamento_com_bonus = faturamento + bonus_formatado
print("\nFaturamento com Bônus (via Broadcasting):\n")
print(faturamento_com_bonus)