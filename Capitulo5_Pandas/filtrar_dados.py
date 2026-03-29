import pandas as pd
dados = {
    'Nome': ['Ana', 'Bruno', 'Fabiana', 'Ronaldo', 'Eliana', 'Matias'],
    'Idade': [28, 34, 29, 17, None, 78],
    'Cidade': ['Blumenau', 'São Paulo', 'Blumenau', 'São Paulo', 'Salvador', 'São Paulo'],
    'Salário': [None, 7500, 6200, 9300, 8100, 15400]
}

df = pd.DataFrame(dados)
## 4. Filtragem de Dados com Pandas

# Você pode filtrar linhas com base em condições lógicas, de forma muito intuitiva, bem como usar colunas como índice.

# Convertendo a coluna zero (nomes) em índice
df = df.set_index(df.columns[0])

# Filtramos usando label do índice (linha) e da coluna
df.loc["Fabiana", "Salário"]

# Podemos aplicar o filtro de forma que retorne um dataframe. Observe a diferença sutil na sintaxe.
df.loc[["Fabiana"], ["Salário"]]

# Reset para retornar o índice ao padrão do Pandas
df = df.reset_index()

# Visualizando as primeiras linhas
df.head(6)

# Filtrando funcionários com idade superior a 30 anos
mais_de_30 = df[df['Idade'] > 30]
print("\n--- Funcionários com mais de 30 anos ---\n")
print(mais_de_30)
print("\n")

# Filtrando funcionários de São Paulo com salário acima de 6000
sp_salario_alto = df[(df['Cidade'] == 'São Paulo') & (df['Salário'] > 6000)]
print("\n--- Funcionários de São Paulo com salário > 6000 ---\n")
print(sp_salario_alto)

# Verificamos quais células têm valores nulos
df.isnull()

# Verificamos se há qualquer valor nulo em cada coluna
df.isnull().any()

# Retorna apenas as colunas que possuem pelo menos um valor nulo
df_colunas_com_nulos = df.loc[:, df.isnull().any()]

df_colunas_com_nulos.head()

# Retorna apenas linhas com valores nulos
df_linhas_com_nulos = df[df.isnull().any(axis = 1)]

df_linhas_com_nulos.head()

# Podemos ainda filtrar pela coluna e então verificar se há valores nulos
linhas_com_nulos_idade = df[df["Idade"].isnull()]

linhas_com_nulos_idade.head()

