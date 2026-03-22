## 9. Operações Matemáticas com Matrizes

import numpy as np

# Criando duas matrizes
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"\nMatriz A:\n{A}\n")
print(f"Matriz B:\n{B}\n")

# Produto de Matrizes (diferente da multiplicação elemento a elemento)
# Usando o operador @
produto_matricial = A @ B
print(f"\nProduto de A por B:\n\n{produto_matricial}\n")

#Nesse trecho acima, são criadas duas matrizes 2×2 chamadas A e B. Em seguida, é realizado o produto matricial entre elas usando o operador @. Diferente da multiplicação elemento a elemento (que faz a operação posição por posição), o produto matricial segue as regras da álgebra linear: cada elemento da matriz resultante é obtido multiplicando os elementos de uma linha da primeira matriz pelos elementos de uma coluna da segunda e somando esses produtos. O cálculo do produto é:
#[ [1 * 5 + 2 * 7, 1 * 6 + 2 * 8], [3 * 5 + 4 * 7, 3 * 6 + 4 * 8] ] = [[19, 22], [43, 50]]

# Usando np.dot() ao invés de @
produto_matricial = np.dot(A, B)
print(f"Produto de A por B:\n{produto_matricial}\n")

#ATENÇÃO: Quando fazemos:

#produto_matricial = A @ B
# ou
# produto_matricial = np.dot(A, B)
 
# Estamos realizando o produto matricial clássico da Álgebra Linear. Cada elemento do resultado é a soma dos produtos entre as linhas de A e as colunas de B.

print(f"\nMatriz A:\n{A}\n")
print(f"Matriz B:\n{B}\n")

# Element wise
produto_element_wise = A * B
print(f"Multiplicação Element-wise de A por B:\n{produto_element_wise}\n")

#ATENÇÃO: Quando fazemos:

# produto_elementwise = A * B

# O NumPy multiplica cada elemento na mesma posição das duas matrizes. Não há soma de produtos; é apenas posição a posição. 

#Normalmente usamos o produto matricial (@ ou np.dot) quando implementamos modelos de Machine Learning ou IA com redes neurais, e não a multiplicação elemento a elemento. Motivo:

# Cada camada de uma rede neural realiza uma transformação linear dos dados de entrada. Essa transformação é feita multiplicando a matriz de pesos da camada (W) pelo vetor ou matriz de entradas (X):
# 
# saída = X @ W + bias
# 
# - X → entradas (amostras × features)
# - W → pesos (features × neurônios)
# - bias → deslocamento adicionado depois
# 
# O resultado é uma nova matriz onde cada neurônio combina as entradas por meio de somas ponderadas. Esse processo só é possível com o produto matricial, porque ele combina cada entrada com todos os pesos de cada neurônio ao mesmo tempo, gerando uma saída que depois passa por uma função de ativação (ReLU, sigmoid, etc.).

#A multiplicação element-wise (*) é usada em redes neurais, mas em casos específicos, como:

#- Hadamard product em algumas arquiteturas (por exemplo, em gates de LSTM/GRU ou atenção em Transformers);
#- Aplicar máscaras ou pesos individuais diretamente em cada elemento.

#Mas a operação central de treino e propagação em redes neurais é sempre o produto matricial, porque ela permite aprender pesos que combinam múltiplas entradas para gerar representações mais complexas.

# Criando duas matrizes 2x2

A = np.array([[10, 20],
              [30, 40]])

B = np.array([[7, 14],
              [4, 3]])

# Soma de matrizes
soma = A + B

# Subtração de matrizes
subtracao = A - B

# Divisão elemento a elemento
divisao = A / B

print("Matriz A:\n", A)
print("\nMatriz B:\n", B)
print("\nSoma A + B:\n", soma)
print("\nSubtração A - B:\n", subtracao)
print("\nDivisão A / B:\n", divisao)