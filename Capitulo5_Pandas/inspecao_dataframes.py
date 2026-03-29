#%%
import pandas as pd
import numpy as np
dados = {
    'Nome': ['Ana', 'Bruno', 'Fabiana', 'Ronaldo', 'Eliana', 'Matias'],
    'Idade': [28, 34, 29, 17, None, 78],
    'Cidade': ['Blumenau', 'São Paulo', 'Blumenau', 'São Paulo', 'Salvador', 'São Paulo'],
    'Salário': [None, 7500, 6200, 9300, 8100, 15400]
}

df = pd.DataFrame(dados)
#%%
## 5. Inspeção de DataFrames do Pandas

# Podemos inspecionar e resumir o dataframe de várias formas.

# Mostra o número de linhas e colunas (formato)
print(f"\n--- Formato do DataFrame (.shape) ---\n{df.shape}")

# Mostra as 3 primeiras linhas do DataFrame
print("\n--- As 3 primeiras linhas (.head(3)) ---\n")
print(df.head(3))
print("\n")

# Mostra as 2 últimas linhas do DataFrame
print("\n--- As 2 últimas linhas (.tail(2)) ---\n")
print(df.tail(2))
print("\n")

# Fornece um resumo conciso do DataFrame (tipos de dados, valores não nulos, etc.)
# Observe a contagem de valores
print("\n--- Informações gerais (.info()) ---\n")
df.info()
print("\n")

#%%
# Gera estatísticas descritivas das colunas numéricas
print("\n--- Estatísticas descritivas (.describe()) ---\n")
print(df.describe())
print("\n")
# %%

print("\n--- Estatísticas descritivas (numéricas e objetos) ---\n")
print(df.describe(include = 'all'))  # inclui números, objetos e categorias

df.describe(include = [object])   # só colunas do tipo object

df.describe(include = [np.number])  # só colunas numéricas (comportamento padrão)