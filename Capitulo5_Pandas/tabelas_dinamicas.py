import pandas as pd
## 9. Criação de Tabelas Dinâmicas (Pivot Tables) com Pandas

# Tabelas dinâmicas são ótimas para resumir dados de forma semelhante a uma planilha.

# Vamos adicionar mais dados para a tabela dinâmica ficar mais interessante
dados_vendas = {
    'Data': pd.to_datetime(['2026-09-01', '2026-09-01', '2026-09-02', '2026-09-02', '2026-09-01']),
    'Região': ['Norte', 'Sul', 'Norte', 'Sul', 'Norte'],
    'Vendedor': ['Carlos', 'Ana', 'Carlos', 'Ana', 'Pedro'],
    'Vendas': [250, 300, 150, 400, 200]
}

# Cria o dataframe
df_vendas = pd.DataFrame(dados_vendas)

# Criando uma tabela dinâmica para ver o total de vendas por Região e Vendedor
tabela_dinamica = df_vendas.pivot_table(values = 'Vendas',index = 'Região',columns = 'Vendedor',aggfunc = 'sum',fill_value = 0)

print("\n--- Tabela Dinâmica: Total de Vendas por Região e Vendedor ---\n")
tabela_dinamica