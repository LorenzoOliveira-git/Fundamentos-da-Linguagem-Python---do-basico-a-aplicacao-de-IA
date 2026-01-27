## 8. Manipulação de Formato de Arrays

#Muitas vezes precisamos reorganizar os dados em um formato diferente para análise ou para alimentar um modelo de IA.

import numpy as np

# Criando um array 1D com 12 elementos
dados_sequenciais = np.arange(12)
print(f"\nArray original (1D): {dados_sequenciais}\n")

# Remodelando para uma matriz 3x4
matriz_3x4 = dados_sequenciais.reshape(3, 4)
print(f"\nMatriz 3x4:\n{matriz_3x4}\n")

# Transpondo a matriz (trocando linhas por colunas)
matriz_transposta = matriz_3x4.T
print(f"\nMatriz Transposta (4x3):\n{matriz_transposta}\n")

# Achatando a matriz de volta para um array 1D
array_achatado = matriz_transposta.flatten()
print(f"\nArray achatado (1D): {array_achatado}")