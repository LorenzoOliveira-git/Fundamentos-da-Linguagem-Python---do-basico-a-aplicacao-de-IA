import pandas as pd
dados = {
    'Nome': ['Ana', 'Bruno', 'Fabiana', 'Ronaldo', 'Eliana', 'Matias'],
    'Idade': [28, 34, 29, 17, None, 78],
    'Cidade': ['Blumenau', 'São Paulo', 'Blumenau', 'São Paulo', 'Salvador', 'São Paulo'],
    'Salário': [None, 7500, 6200, 9300, 8100, 15400]
}

df = pd.DataFrame(dados)

## 3. Seleção e Indexação com Pandas

# Existem várias maneiras de selecionar dados de um DataFrame. As mais comuns são loc (baseado em rótulo) e iloc (baseado em posição/índice numérico).

# Visualizando as primeiras linhas
df.head(6)

# Selecionando uma única coluna (retorna uma Series)
nomes = df['Nome']
print("\n--- Selecionando a coluna 'Nome' ---\n")
print(nomes)
print("\n")

type(nomes)

# Selecionando múltiplas colunas (retorna um DataFrame)
info_pessoal = df[['Nome', 'Idade']]
print("\n--- Selecionando as colunas 'Nome' e 'Idade' ---\n")
print(info_pessoal)
print("\n")

type(info_pessoal)

# Usando .loc para selecionar pela linha (rótulo/índice 1) e coluna ('Nome')
nome = df.loc[1, 'Nome']
print(f"\n--- Selecionando com .loc[1, 'Nome'] ---\n{nome}\n")

# Usando .iloc para selecionar pela posição da linha (linha 2) e da coluna (coluna 3)
salario_fabiana = df.iloc[2, 3]
print(f"\n--- Selecionando com .iloc[2, 3] ---\n{salario_fabiana}\n")

# Selecionando um intervalo de linhas
primeiras_tres_linhas = df.loc[0:2] # O final (2) é inclusivo com .loc
print("\n--- Selecionando as 3 primeiras linhas com .loc ---\n")
print(primeiras_tres_linhas)



