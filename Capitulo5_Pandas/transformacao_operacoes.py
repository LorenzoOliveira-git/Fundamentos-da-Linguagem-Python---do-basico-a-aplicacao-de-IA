import pandas as pd
import numpy as np
dados = {
    'Nome': ['Ana', 'Bruno', 'Fabiana', 'Ronaldo', 'Eliana', 'Matias'],
    'Idade': [28, 34, 29, 17, None, 78],
    'Cidade': ['Blumenau', 'São Paulo', 'Blumenau', 'São Paulo', 'Salvador', 'São Paulo'],
    'Salário': [None, 7500, 6200, 9300, 8100, 15400]
}

df = pd.DataFrame(dados)

## 6. Operações e Transformações de Dados com Pandas

# Você pode facilmente criar novas colunas a partir de outras ou aplicar funções para modificar os dados. Fazemos isso com frequência em tarefas de engenharia de atributos em projetos de Ciência de Dados.

# Criando uma nova coluna 'Salário Anual'
df['Salário Anual'] = df['Salário'] * 12
print("\n--- DataFrame com a nova coluna 'Salário Anual' ---\n")
print(df)
print("\n")

df['Bônus'] = df['Salário'].apply(lambda x: x * 0.10 if x > 7000 else x * 0.05)
print("\n--- DataFrame com a nova coluna 'Bônus' ---\n")
print(df)

# Vamos criar uma coluna de faixa etária.

# Define as condições (vamos criar o que chamamos de máscara)
condicoes = [
    df['Idade'] < 18,
    (df['Idade'] >= 18) & (df['Idade'] <= 30),
    (df['Idade'] > 30) & (df['Idade'] <= 60),
    df['Idade'] > 60
]

# Define os rótulos correspondentes
faixas = ['Menor de idade', 'Jovem', 'Adulto', 'Idoso']

# Cria a nova coluna
df['Faixa Etária'] = np.select(condicoes, faixas, default = 'Idade não informada')

df.head(6)
