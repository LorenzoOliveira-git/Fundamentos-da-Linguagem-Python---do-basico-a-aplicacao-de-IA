# 1. Tomada de Decisão com Estruturas Condicionais

#As estruturas condicionais (if, elif, else) permitem que o programa execute diferentes blocos de código com base em certas condições.

#Exemplo 1:
# Define a variável
nota = 8.5

# Agora checamos o valor da variável e tomamos decisões
if nota >= 7.0:
    print("Aprovado!")
else:
    print("Reprovado.")

#Exemplo 2:
# Define a variável
idade = 100

# Agora checamos o valor da variável e tomamos decisões
if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade < 65:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")