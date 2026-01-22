#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random as rd
from datetime import datetime, timedelta

# Definição da função para gerar dados fictícios de vendas
def gerar_dados_ficticios(num_registros = 600):
    produtos = {
        'Laptop Gamer': {'categoria': 'Eletrônicos', 'preco': 7500.00},
        'Mouse Vertical': {'categoria': 'Acessórios', 'preco': 250.00},
        'Teclado Mecânico': {'categoria': 'Acessórios', 'preco': 550.00},
        'Monitor Ultrawide': {'categoria': 'Eletrônicos', 'preco': 2800.00},
        'Cadeira Gamer': {'categoria': 'Móveis', 'preco': 1200.00},
        'Headset 7.1': {'categoria': 'Acessórios', 'preco': 800.00},
        'Placa de Vídeo': {'categoria': 'Hardware', 'preco': 4500.00},
        'SSD 1TB': {'categoria': 'Hardware', 'preco': 600.00}
    }

    lista_produtos = list(produtos.keys())

    cidades_estados = {
        'São Paulo': 'SP', 'Rio de Janeiro': 'RJ', 'Belo Horizonte': 'MG',
        'Porto Alegre': 'RS', 'Salvador': 'BA', 'Curitiba': 'PR', 'Fortaleza': 'CE'
    }

    lista_cidades = list(cidades_estados.keys())

    dados_vendas = []

    data_inicial = datetime(year=2026,month=1 ,day=20)

    # Loop para gerar os registros de vendas
    for i in range(num_registros):
        
        produto_nome = rd.choice(lista_produtos)

        cidade = rd.choice(lista_cidades)

        quantidade = np.random.randint(1, 8)

#Data inicial = 20/01/2026 e vai somar com a quantidade de dias determinada pelo argumento days = int(i/5), mudando com o passar a iteração do loop for, e as horas que são aleatórias pelo random.randint
#Esse módulo do datetime juntamente com o método timedelta é muito bom para somar datas e horários.
        data_pedido = data_inicial + timedelta(days = int(i/5), hours = rd.randint(0, 23))

        # Se o produto for Mouse ou Teclado, aplica desconto aleatório de até 10%
        if produto_nome in ['Mouse Vertical', 'Teclado Mecânico']:
            preco_unitario = produtos[produto_nome]['preco'] * np.random.uniform(0.9, 1.0)
        else:
            preco_unitario = produtos[produto_nome]['preco']

        dados_vendas.append({
            'ID_Pedido': 1000 + i,
            'Data_Pedido': data_pedido,
            'Nome_Produto': produto_nome,
            'Categoria': produtos.get(produto_nome).get("categoria"),
            'Preco_Unitario': round(preco_unitario, 2),
            'Quantidade': quantidade,
            'ID_Cliente': np.random.randint(100, 150),
            'Cidade': cidade,
            'Estado': cidades_estados.get(cidade)
        })

    # Retorna os dados no formato de DataFrame
    return pd.DataFrame(dados_vendas)

df_vendas = gerar_dados_ficticios(500)

#----------------------------------------------------
#LIMPEZA, PRÉ-PROCESSAMENTO E ENGENHARIA DE ATRIBUTOS

#CASO 1:
#Se a coluna 'Data_Pedido' não estiver como datatime, precimos fazer a conversão explícita
df_vendas.dtypes

df_vendas["Data_Pedido"] = pd.to_datetime(df_vendas['Data_Pedido'])
df_vendas.dtypes

#CASO 2:
#Engenharia de atributos - tem por objetivo transformar os dados inplicitos em explicitos para melhor performance de análise
#Tendo em vista que um dos problemas de negócio é saber a receita total do faturamento de cada produto, temos uma problema com os dados que temos agora, não temos uma coluna explícita indicando o faturamento por venda, então resolveremos isso criando uma nova coluna que indica a quantidade vendida do produto * preço unitário
df_vendas['Faturamento'] = df_vendas["Quantidade"] * df_vendas["Preco_Unitario"]
df_vendas.head()

#CASO 3:
#Engenharia de atributos
#Vamos criar uma nova coluna que indica o tempo de velocidade da entrega com base na cidade em que a venda foi efetuada.
df_vendas["Status_Entrega"] = df_vendas["Estado"].map(lambda estado: "Rápido" if estado in ["SP","RJ","MG"] else "Normal")
df_vendas.head()

#----------------------------------------------------

#ANÁLISE 1

#Top 10 produtos mais vendidos

df_top_10 = df_vendas.groupby(["Nome_Produto"])["Quantidade"].sum().sort_values(ascending=False).head(10)

sns.set_style("whitegrid")

plt.figure(figsize=(12,7))

df_top_10.sort_values(ascending=True).plot(kind="barh",color="skyblue")

plt.title('Top 10 Produtos Mais Vendidos',fontsize=12)
plt.xlabel('Quantidade Vendida',fontsize=12)
plt.ylabel('Produto',fontsize=12)

plt.savefig("imagens/analise_vendas")
plt.show()


#ANÁLISE 2

#Qual foi o faturamento mensal?

#Engenharia de atributos
#.dt.to_period corta a data pelo mes, ano ou dia.
df_vendas["Mes"] = df_vendas["Data_Pedido"].dt.to_period("M")

faturamento_mensal = df_vendas.groupby(["Mes"])['Faturamento'].sum()

#Converter o índice para string para facilitar a plotagem do gráfico
faturamento_mensal.index = faturamento_mensal.index.strftime('%Y-%m')

#Formatar para duas casas decimais
faturamento_mensal.map(lambda faturamento: round(faturamento,2))

#gráfico
plt.figure(figsize=(12,6))

faturamento_mensal.plot(kind="line", marker = "o", linestyle= '-', color="green")

plt.title("Evolução do Faturamento Mensal", fontsize=16)

plt.xlabel('Mês',fontsize=12)
plt.ylabel('Faturamento (R$)',fontsize=12)

#Rotacionar os valores do eixo X em 45 graus para melhor visualização
plt.xticks(rotation=45)

plt.grid(True, which="both", linestyle="--",linewidth=0.5)

plt.tight_layout()
plt.savefig("imagens/faturamento_mensal")
plt.show()


#ANÁLISE 3

#Qual é o faturamento total de cada estado?

vendas_estado = df_vendas.groupby(["Estado"])["Faturamento"].sum().sort_values(ascending=False)

#Formatar com duas casas decimais
vendas_estado.map(lambda faturamento: round(faturamento, 2))


#gráfico

plt.figure(figsize=(12,7))

#Essa color_palette vem da documentação do seaborn
vendas_estado.plot(kind="bar", color = sns.color_palette("husl",7))

plt.title("Faturamento Por Estado",fontsize=16)
plt.xlabel("Estado",fontsize=12)
plt.ylabel("Faturamento (R$)",fontsize=12)

plt.tight_layout()

plt.savefig("imagens/vendas_estados")
plt.show()


#ANÁLISE 4

#Faturamento total por categoria?

faturamento_categoria = df_vendas.groupby(["Categoria"])["Faturamento"].sum().sort_values(ascending=False)

#Engenharia de dados - modificar o faturamento total para 2 casas decimais
faturamento_categoria.map(lambda faturamento: round(faturamento,2))

#Gráfico

from matplotlib.ticker import FuncFormatter

fig, ax = plt.subplots(figsize = (12,7))

def formatador_milhares(y,pos):
    return f'RS {y/1000:,.0f}K'

formatter = FuncFormatter(formatador_milhares)

ax.yaxis.set_major_formatter(formatter)

faturamento_categoria.plot(kind="bar",ax=ax,color=sns.color_palette("viridis",len(faturamento_categoria)))

ax.set_title("Faturamento por Categoria",fontsize=16)
ax.set_xlabel("Categoria",fontsize=12)
ax.set_ylabel("Faturamento (R$)",fontsize=12)

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("imagens/faturamento_categoria")
plt.show()

# %%
