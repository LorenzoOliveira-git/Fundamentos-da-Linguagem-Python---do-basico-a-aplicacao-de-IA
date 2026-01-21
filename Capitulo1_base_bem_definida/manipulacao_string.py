## 6. Manipulação de Strings

#Strings são sequências de caracteres e possuem muitos métodos úteis.

# Define uma variável do tipo string
frase = "  Aprender Python é muito divertido!  "

# Concatenação
nome = "Maria"
saudacao = "Olá, " + nome + "!"
print(saudacao)

# Tamanho da string
print(f"Tamanho da frase: {len(frase)}")

# Maiúsculas e Minúsculas
print(f"Maiúsculas: {frase.upper()}")
print(f"Minúsculas: {frase.lower()}")

# Remover espaços em branco do início e do fim
frase_sem_espacos = frase.strip()
print(f"Frase sem espaços: '{frase_sem_espacos}'")

# Substituir texto
print(f"Substituindo 'divertido' por 'legal': {frase_sem_espacos.replace('divertido', 'legal')}")

print(f"Frase sem espaços: '{frase_sem_espacos}'")

# Fatiamento (Slicing) - Acessando partes de uma string
# O índice em Python começa em 0
print(frase_sem_espacos)
print(f"O primeiro caractere: {frase_sem_espacos[0]}")
print(f"A palavra 'Python': {frase_sem_espacos[9:15]}") # Do índice 9 ao 14