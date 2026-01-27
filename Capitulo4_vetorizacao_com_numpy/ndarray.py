## 2. O Objeto ndarray

#Um array NumPy é uma estrutura de dados multidimensional usada em computação científica e análise de dados. O NumPy fornece um objeto de matriz N-dimensional (ou ndarray), que é uma grade homogênea de elementos, geralmente números, que podem ser indexados por um conjunto de inteiros.

#Os arrays NumPy são mais eficientes do que as listas Python para armazenar e manipular grandes quantidades de dados, pois são implementados em Linguagem C e fornecem várias otimizações de desempenho. Além disso, o NumPy permite a fácil leitura e escrita de arquivos de dados, integração com outras bibliotecas Python e suporte a operações em paralelo usando várias CPUs ou GPUs.

#A principal estrutura do numpy para vetorização dos dados é o ndarray (array n-dimensional). Para cada quantidade de dimensões dentro do seu array, associa-se um nome diferente:

#1D - vetor
#2D - matriz
#3D ou mais - tensor

#É importante lembrar que as principais ferramentas de análise e ciência de dados que os profissionais usam hoje são feitas com o numpy, entre elas temos o tensoflow, pytorch, pandas, etc.

import numpy as np

# Criando um array de 1 dimensão (vetor) a partir de uma lista Python
vetor = np.array([17, 21, 100, 34])
print("\nVetor (Array 1D):\n")
print(vetor)

# Verificando atributos 
print("Formato (shape) do vetor:", vetor.shape) 
print("Número de dimensões (ndim) do vetor:", vetor.ndim)
print("Número total de elementos (size) do vetor:", vetor.size)

# Criando um array de 2 dimensões (matriz) a partir de uma lista de listas
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print("\nMatriz (Array 2D):\n")
print(matriz)

# Verificando atributos 
print("Formato (shape) da matriz:", matriz.shape)  # (linhas, colunas)
print("Número de dimensões (ndim) da matriz:", matriz.ndim)
print("Número total de elementos (size) da matriz:", matriz.size)

# Criando um array 3D usando np.arange()
arr = np.arange(24).reshape(4, 3, 2)
print("\nArray (Array 3D):\n")
print(arr)

# Verificando atributos 
print("Formato (shape) do array:", arr.shape) 
print("Número de dimensões (ndim) do array:", arr.ndim)
print("Número total de elementos (size) do array:", arr.size)

#Array 3D — Um array com três eixos, sendo: shape = (profundidade, linhas, colunas) ou (altura, largura, canais) em imagens. 

#Tensor 3D — Em Machine Learning e computação numérica, um tensor de ordem 3 é, de fato, um array 3D.

# Array 4D com valores sequenciais de 0 a 119 organizado em 2x3x4x5 (2 blocos, 3 "planos", 4 linhas, 5 colunas)
tensor_4d = np.arange(120).reshape(2, 3, 4, 5)
print(tensor_4d)  

# Verificando atributos importantes do array
print("Formato (shape) do array:", tensor_4d.shape) 
print("Número de dimensões (ndim) do array:", tensor_4d.ndim)
print("Número total de elementos (size) do array:", tensor_4d.size)
