import pandas as pd
import numpy as np
dados = {
    'Nome': ['Ana', 'Bruno', 'Fabiana', 'Ronaldo', 'Eliana', 'Matias'],
    'Idade': [28, 34, 29, 17, None, 78],
    'Cidade': ['Blumenau', 'São Paulo', 'Blumenau', 'São Paulo', 'Salvador', 'São Paulo'],
    'Salário': [None, 7500, 6200, 9300, 8100, 15400]
}

df = pd.DataFrame(dados)

## 7. Agrupamento de Dados (Group By) com Pandas

# O método groupby é extremamente poderoso para análises segmentadas. É exatamente o mesmo conceito usado em Linguagem SQL.

# Agrupando os dados por 'Cidade' e calculando a média de 'Salário' para cada cidade
media_salario_cidade = df.groupby('Cidade')['Salário'].mean()
print("\n--- Média de Salário por Cidade ---\n")
print(np.round(media_salario_cidade,2))
print("\n")

# Agrupando por cidade e calculando múltiplas agregações
agregacao_cidade = df.groupby('Cidade').agg(Media_Salarial = ('Salário', 'mean'),
                                                Idade_Maxima = ('Idade', 'max'),
                                                Contagem = ('Nome', 'count'))

print("\n--- Agregação múltipla por Cidade ---\n")
print(agregacao_cidade)