## 5. Operadores Aritméticos, de Comparação e Lógicos

# 5.1. Operadores Aritméticos
#Usados para realizar operações matemáticas.

# Definição de variáveis
a = 10
b = 3

# Usando operadores aritméticos
soma = a + b              # Adição
subtracao = a - b         # Subtração
multiplicacao = a * b     # Multiplicação
divisao = a / b           # Divisão (resultado é sempre float)
divisao_inteira = a // b  # Divisão inteira (descarta a parte decimal)
modulo = a % b            # Módulo (resto da divisão)
potencia = a ** b         # Potenciação

print(f"{a} + {b} = {soma}")
print(f"{a} - {b} = {subtracao}")
print(f"{a} * {b} = {multiplicacao}")
print(f"{a} / {b} = {divisao:.2f}")
print(f"{a} // {b} = {divisao_inteira}")
print(f"{a} % {b} = {modulo}")

# As regras da matemática de aplicam aqui normalmente

# Variáveis
a = 10
b = 0
# Tentativa de divisão por zero
# a/b

# Cuidado. Isso não pode!
# 8 + 's'
# Mas isso pode! (não é soma, é concatenação)
'8' + 's' 

# ------------------------------------------------------------------------------------------

# 5.2. Operadores de Comparação

#Usados para comparar valores. O resultado é sempre um Boolean (True ou False).
# Definição de variáveis
x = 5
y = 10

# Operador "maior que"
x > y

# Operador "menor que"
x < y

# Operador "igual a"
x == y

# Operador "diferente de"
x != y

# Operador "maior ou igual a"
x >= 5

# Operador "menor ou igual a"
x <= y

print(f"{x} > {y} ? {x > y}")      # Maior que
print(f"{x} < {y} ? {x < y}")      # Menor que
print(f"{x} == {y} ? {x == y}")    # Igual a
print(f"{x} != {y} ? {x != y}")    # Diferente de
print(f"{x} >= 5 ? {x >= 5}")      # Maior ou igual a
print(f"{x} <= {y} ? {x <= y}")    # Menor ou igual a

# ------------------------------------------------------------------------------------------

# 5.3. Operadores Lógicos

#Usados para combinar expressões booleanas.

# Definição de variáveis
tem_dinheiro = True
tem_tempo = False

# Operador AND (e): Ambos precisam ser verdadeiros
print(f"O cliente pode viajar? {tem_dinheiro and tem_tempo}")

# Operador OR (ou): Pelo menos um precisa ser verdadeiro
print(f"O cliente pode viajar? {tem_dinheiro or tem_tempo}")

## Operador NOT (não): Inverte o valor booleano
print(f"O cliente pode viajar? {tem_dinheiro and not tem_tempo}")