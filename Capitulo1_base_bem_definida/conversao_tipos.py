## 11. Conversão Entre Tipos de Dados (Type Casting)

#É a conversão de um tipo de dado para outro.

# Convertendo de string para número integer
numero_em_texto = "123"
numero_inteiro = int(numero_em_texto)
print(f"String '{numero_em_texto}' para Inteiro: {numero_inteiro}, Tipo: {type(numero_inteiro)}")

# Isso aqui não pode ser feito
# teste = "Esta é uma string de teste"
# teste_int = int(teste)
# print(teste_int)

# Convertendo de string para número float
numero_decimal_em_texto = "45.67"
numero_float = float(numero_decimal_em_texto)
print(f"String '{numero_decimal_em_texto}' para Float: {numero_float}, Tipo: {type(numero_float)}")

# Convertendo de número para string
idade = 25
idade_texto = str(idade)
print(f"Inteiro {idade} para String: '{idade_texto}', Tipo: {type(idade_texto)}")

# Convertendo entre estruturas de dados
lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 4, 5]
conjunto_unico = set(lista_com_duplicatas)
lista_sem_duplicatas = list(conjunto_unico)

print(f"\nLista original: {lista_com_duplicatas}")
print(f"\nConvertida para Conjunto (remove duplicatas): {conjunto_unico}")
print(f"\nConvertida de volta para Lista: {lista_sem_duplicatas}\n")