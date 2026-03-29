import pandas as pd
import numpy as np
dados = {
    'Nome': ['Ana', 'Bruno', 'Fabiana', 'Ronaldo', 'Eliana', 'Matias'],
    'Idade': [28, 34, 29, 17, None, 78],
    'Cidade': ['Blumenau', 'São Paulo', 'Blumenau', 'São Paulo', 'Salvador', 'São Paulo'],
    'Salário': [None, 7500, 6200, 9300, 8100, 15400]
}

df = pd.DataFrame(dados)

## 8. Manipulação de Tipos de Dados com Pandas

# Garantir que cada coluna tenha o tipo de dado correto é fundamental para qualquer tipo de análise.

# Verificando os tipos de dados atuais
print("\n--- Tipos de dados antes da conversão ---\n")
print(df.dtypes)
print("\n")

# Convertendo a coluna 'Idade' de float64 para int64 - ATENÇÃO!!!!!
#df['Idade'] = df['Idade'].astype(int)
# Essa conversão resultará em erro em razão de valores faltantes na base de dados.

# Primeiro removemos a linha com valor ausente
df = df.dropna(subset = ['Idade'])

# E então fazemos a conversão
df['Idade'] = df['Idade'].astype(int)

print("\n--- Tipos de dados após a conversão ---\n")
print(df.dtypes)

# Convertendo do tipo object para o tipo string
df['Nome'] = df['Nome'].astype('string')
df['Cidade'] = df['Cidade'].astype('string')
df['Faixa Etária'] = df['Faixa Etária'].astype('string')

print("\n--- Tipos de dados após a conversão ---\n")
print(df.dtypes)

df = df.astype({col:'string' for col in df.select_dtypes(include='object').columns})

print("\n--- Tipos de dados após a conversão ---\n")
print(df.dtypes)

# Diferença entre object e string no pandas:

# - object é um tipo genérico que armazena qualquer coisa em Python (strings, números, listas, etc.).

# - string (desde o Pandas 1.0) é um tipo de dado nativo para texto, pensado para operações mais seguras e consistentes com strings.

# Com string, você ganha melhor integração com métodos de texto (.str) e tratamento explícito de valores ausentes (< NA > em vez de NaN misturado com objetos).

# Em grandes DataFrames, o tipo string pode ser um pouco mais eficiente e evita confusões quando colunas deveriam ser só texto. Mas não é obrigatório converter, mas usar string ajuda a ter consistência, evitar misturar tipos diferentes na mesma coluna e facilita operações textuais. Para análises e limpeza de dados de texto, geralmente vale a pena.

