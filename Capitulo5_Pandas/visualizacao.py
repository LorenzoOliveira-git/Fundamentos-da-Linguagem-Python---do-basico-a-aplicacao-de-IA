import pandas as pd
import matplotlib.pyplot as plt
## 10. Visualizações de Dados com Pandas e Matplotlib

# O Pandas se integra perfeitamente com o Matplotlib para criar visualizações diretamente do DataFrame.

# Carrega novamente o dataframe inicial
df = pd.read_csv('dados_funcionarios_sem_indice.csv')

# Calcula a média de salário por cidade
media_salario_cidade = df.groupby('Cidade')['Salário'].mean()

# Gráfico de Barras: Média de Salário por Cidade
media_salario_cidade.plot(kind = 'bar', figsize = (12, 5), color = 'skyblue')

# Adicionando títulos e rótulos
plt.title('Média Salarial Por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Média de Salário (R$)')
plt.xticks(rotation = 45) 
plt.grid(axis = 'y', linestyle = '--')

# Mostra o gráfico
plt.show()

# Contagem de registros (funcionários) por cidade
contagem_cidade = df['Cidade'].value_counts()

# Gráfico de Pizza: Contagem de funcionários por cidade
contagem_cidade.plot(kind = 'pie', autopct = '%1.1f%%', figsize = (6, 6), startangle = 90)
plt.title('Distribuição de Funcionários Por Cidade')
plt.ylabel('') # Remove o rótulo do eixo y
plt.show()