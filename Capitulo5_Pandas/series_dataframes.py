## 1- Pandas e Estruturas de Dados - Series e DataFrame

# Vamos começar criando as estruturas de dados fundamentais: Series e DataFrame.

# No Pandas, uma Series (uma série) é uma estrutura unidimensional, parecida com uma coluna de uma tabela: contém uma sequência de valores com um índice associado. Já um DataFrame é uma estrutura bidimensional, semelhante a uma planilha, tabela ou matriz, formada por várias colunas (que são, internamente, Series alinhadas pelo mesmo índice).

#%%
import pandas as pd
# Criando uma Series (uma única coluna)
s = pd.Series([10, 20, 30, 40, 50], name = 'Valores')

type(s)

print("\n--- Exemplo de Series ---\n")
print(s)
print("\n")

#%%

# Criamos um dicionário em Python (observe que alguns valores estão nulos representados como None)
dados = {
    'Nome': ['Ana', 'Bruno', 'Fabiana', 'Ronaldo', 'Eliana', 'Matias'],
    'Idade': [28, 34, 29, 17, None, 78],
    'Cidade': ['Blumenau', 'São Paulo', 'Blumenau', 'São Paulo', 'Salvador', 'São Paulo'],
    'Salário': [None, 7500, 6200, 9300, 8100, 15400]
}

type(dados)

print(dados)

# Convertemos o dicionário em um dataframe do pandas
df = pd.DataFrame(dados)

type(df)

print("\n--- Exemplo de DataFrame ---\n")
print(df)