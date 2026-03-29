#%%
import pandas as pd

dados = {
    'Nome': ['Ana', 'Bruno', 'Fabiana', 'Ronaldo', 'Eliana', 'Matias'],
    'Idade': [28, 34, 29, 17, None, 78],
    'Cidade': ['Blumenau', 'São Paulo', 'Blumenau', 'São Paulo', 'Salvador', 'São Paulo'],
    'Salário': [None, 7500, 6200, 9300, 8100, 15400]
}

df = pd.DataFrame(dados)

## 2- Leitura e Escrita de Dados no Formato CSV

# Pandas torna muito fácil salvar seu DataFrame em um arquivo CSV e carregá-lo de volta.

# Escrevendo (salvando) o DataFrame em um arquivo CSV
# index=False evita que o índice do DataFrame seja salvo como uma coluna no CSV
df.to_csv('dados_funcionarios_sem_indice.csv', index = False, encoding = 'utf-8')

# index=True (valor padrão) inclui o índice do DataFrame como uma coluna no CSV
df.to_csv('dados_funcionarios_com_indice.csv', encoding = 'utf-8')

# Lendo dados de um arquivo CSV para um novo DataFrame
df_1 = pd.read_csv('dados_funcionarios_sem_indice.csv')

# Visualizando as primeiras linhas
df_1.head(6)

# Lendo dados de um arquivo CSV para um novo DataFrame
df_2 = pd.read_csv('dados_funcionarios_com_indice.csv')

# Visualizando as primeiras linhas
df_2.head(6)

# Deletando a coluna de índice 0
df_2 = df_2.drop(df_2.columns[0], axis = 1)

# Visualizando as primeiras linhas
df_2.head(6)
# %%
