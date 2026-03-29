#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from generate_data import generate_data

dados_ecommerce = generate_data()

#Passo a passo para análise estatística:
#- Análise da base de dados utilizadas (ver o nome dos campos, significados e dintinções de variável quantitativa ou qualitativa)
#- Limpeza dos dados (Vão ser feitos posteriormente no aprendizado de pandas)
#- Separação das variáveis (para o numpy neste caso)
#- Cálculo estatístico para entrega de valor ao negócio
#- Gráfico representativo do resultado encontrado (opcional)
#- Texto formal que mostra os resultados alcançados com a análise. Geralmente, é importante mostrar o resultado de cada pergunta e recomendações gerais para o tomador de decisão a partir das respostas alcançadas com as análises. Entenda o seu público alvo para saber o que mostrar ao tomador de decisão.

### Pergunta 1

# Qual é o perfil médio do nosso usuário em termos de visitas, tempo de navegação e valor de compra (ticket médio)?

visitas_col = dados_ecommerce[:, 0]
tempo_col   = dados_ecommerce[:, 1]
itens_col   = dados_ecommerce[:, 2]
valor_col   = dados_ecommerce[:, 3]

print("--- ANÁLISE ESTATÍSTICA GERAL ---")

# Média
media_visitas = np.mean(visitas_col)
media_tempo   = np.mean(tempo_col)
media_itens   = np.mean(itens_col)
media_valor   = np.mean(valor_col)

print(f"\nMédia de Visitas: {media_visitas:.2f}")
print(f"Média de Tempo no Site: {media_tempo:.2f} min")
print(f"Média de Itens no Carrinho: {media_itens:.2f}")
print(f"Média de Valor de Compra (Ticket Médio): R$ {media_valor:.2f}")

# Mediana (valor central, menos sensível a outliers)
mediana_valor = np.median(valor_col)
print(f"\nMediana do Valor de Compra: R$ {mediana_valor:.2f}")

# Desvio Padrão (mede a dispersão dos dados)
std_valor = np.std(valor_col)
print(f"Desvio Padrão do Valor de Compra: R$ {std_valor:.2f}")

# Valores Máximos e Mínimos
max_valor = np.max(valor_col)
min_valor_positivo = np.min(valor_col[valor_col > 0]) # Mínimo apenas entre quem comprou
print(f"Maior Valor de Compra: R$ {max_valor:.2f}")
print(f"Menor Valor de Compra (de quem comprou): R$ {min_valor_positivo:.2f}")

# --- GRÁFICO ---
# Gráfico de histograma para análise da variável valor de compra.
plt.figure(figsize = (12, 5))
plt.hist(valor_col, bins = 30, color = 'skyblue', edgecolor = 'black', alpha = 0.7)
plt.axvline(media_valor, color = 'red', linestyle = '--', linewidth = 2, label = f'Média = R$ {media_valor:.2f}')
plt.axvline(mediana_valor, color = 'orange', linestyle = '--', linewidth = 2, label = f'Mediana = R$ {mediana_valor:.2f}')
plt.axvline(media_valor + std_valor, color = 'green', linestyle = ':', linewidth = 2, label = f'+1 DP = R$ {media_valor + std_valor:.2f}')
plt.axvline(media_valor - std_valor, color = 'green', linestyle = ':', linewidth = 2, label = f'-1 DP = R$ {media_valor - std_valor:.2f}')
plt.title('Distribuição dos Valores de Compra')
plt.xlabel('Valor da Compra (R$)')
plt.ylabel('Frequência')
plt.legend()
plt.grid(alpha = 0.3)
plt.show()

# Resposta da Pergunta 1:

# O usuário acessa o site, em média, cerca de 26 vezes por mês, permanece em média 33 minutos navegando, adiciona aproximadamente 7 itens ao carrinho e realiza compras com ticket médio de R$ 252,70. 
# O gasto típico fica próximo da mediana de R$ 248,13.
# Mas há grande variação entre clientes, alguns compram valores baixos a partir de R$ 23,42. 
# Enquanto outros chegam a gastar até R$ 530,37.

#%%

### Pergunta 2

# Quais são as características e comportamentos distintos dos nossos clientes de "Alto Valor"? Eles visitam mais o site? Passam mais tempo navegando?

clientes_alto_valor = dados_ecommerce[dados_ecommerce[:,3] > 250]

print("\n--- ANÁLISE: CLIENTES DE ALTO VALOR (Compras > R$ 250) ---\n")
print(f"Número de clientes de alto valor: {clientes_alto_valor.shape[0]}")

# Estatísticas deste segmento
media_visitas_alto_valor = np.mean(clientes_alto_valor[:, 0])
media_tempo_alto_valor = np.mean(clientes_alto_valor[:, 1])

print(f"Média de visitas desses clientes: {media_visitas_alto_valor:.2f}")
print(f"Média de tempo no site desses clientes: {media_tempo_alto_valor:.2f} min")

# Resposta da Pergunta 2:

# Os clientes de alto valor (aqueles que gastam mais de R$ 250) visitam o site com maior frequência, em média 33 vezes por mês, e permanecem mais tempo navegando, cerca de 37 minutos por sessão. Esse comportamento indica um alto nível de engajamento, sugerindo que quanto mais esses usuários interagem com a plataforma, maior tende a ser o valor de suas compras.

### Pergunta 3

# Qual é o comportamento dos usuários que visitam o site, mas não realizam nenhuma compra? Onde está a oportunidade de conversão com este grupo?

# Filtro para visitantes que não compraram
visitantes_sem_compra = dados_ecommerce[dados_ecommerce[:, 3] == 0]

print("\n--- ANÁLISE: VISITANTES QUE NÃO COMPRAM ---\n")
print(f"Número de visitantes que não compraram: {visitantes_sem_compra.shape[0]}")

# Estatísticas deste segmento
media_tempo_sem_compra = np.mean(visitantes_sem_compra[:, 1])
media_visitas_sem_compra = np.mean(visitantes_sem_compra[:, 0])

print(f"Média de visitas desses visitantes: {media_visitas_sem_compra:.2f}")
print(f"Apesar de não comprarem, eles passam em média {media_tempo_sem_compra:.2f} min no site.")

# Resposta da Pergunta 3:

# Os usuários que não realizam compras visitam o site em média 7 vezes e permanecem cerca de 15 minutos navegando, mas não finalizam nenhuma transação. Esse comportamento mostra que, mesmo com algum nível de interesse, eles acabam desistindo antes da compra, representando uma oportunidade para ações de remarketing, otimização do checkout e estratégias de incentivo, como descontos ou frete grátis, para aumentar a conversão.

### Análise de Correlação

# Vamos investigar a relação entre as diferentes variáveis. Uma matriz de correlação nos mostra como as variáveis se movem juntas.

# - +1: Correlação positiva perfeita
# - -1: Correlação negativa perfeita
# - 0: Nenhuma correlação linear

#%%

### Pergunta 4

# Existe uma correlação estatisticamente relevante entre o tempo gasto no site, o número de itens no carrinho e o valor final da compra?

# A função np.corrcoef calcula a matriz de correlação
# rowvar=False indica que as colunas são as variáveis
matriz_correlacao = np.corrcoef(dados_ecommerce, rowvar = False)

print("\n--- MATRIZ DE CORRELAÇÃO ---\n")
print("[Visitas, Tempo, Itens, Valor]\n")
print(np.round(matriz_correlacao, 2))

# Calcula a matriz de correlação
matriz_correlacao = np.corrcoef(dados_ecommerce, rowvar = False)

# Define os nomes das variáveis
nomes_variaveis = ["Visitas", "Tempo no Site", "Itens no Carrinho", "Valor da Compra"]

# Converte em DataFrame para exibir com rótulos
df_correlacao = pd.DataFrame(matriz_correlacao, 
                             index = nomes_variaveis, 
                             columns = nomes_variaveis)

# Matriz de correlação (mapa de calor)
plt.figure(figsize = (7, 5))
sns.heatmap(df_correlacao, annot = True, cmap = "Blues", fmt = ".2f")
plt.title("Matriz de Correlação")
plt.show()

# Resposta da Pergunta 4:

# A matriz está organizada na ordem [Visitas, Tempo, Itens, Valor]. Os valores variam entre –1 e +1, onde:

# - +1 indica correlação positiva perfeita
# - 0 indica ausência de correlação
# - –1 indica correlação negativa perfeita

# No trecho relevante para a pergunta:

# - Tempo ↔ Valor = 0,59 → correlação positiva moderada

# - Itens ↔ Valor = 1,00 → correlação positiva perfeita (neste conjunto de dados, valor cresce proporcionalmente ao número de itens)

# - Tempo ↔ Itens = 0,60 → correlação positiva moderada

# Esses números indicam que quanto mais tempo o usuário passa no site, maior tende a ser o número de itens no carrinho e, consequentemente, maior o valor da compra. O fato de “Itens ↔ Valor” ser 1,00 mostra que, no dataset analisado, o valor final cresce linearmente com a quantidade de itens (possivelmente porque cada item tem preço médio semelhante).

# Assim, a resposta para a pergunta seria:

# - Sim. Há uma correlação estatisticamente relevante: o tempo gasto no site se relaciona moderadamente tanto com o número de itens no carrinho quanto com o valor final da compra, e a quantidade de itens tem correlação praticamente perfeita com o valor final, indicando forte relação entre esses fatores.

# Obs: Para confirmar a significância estatística, seria necessário calcular o p-valor dessas correlações.

# Nota: Correlação não implica causalidade. Não é porque uma variável tem correlação com outra, que uma variável está causando a outra. Para investigar a causa teríamos que fazer uma Análise Causal.

# %%

# --- RELATÓRIO FINAL ---

# A análise estatística dos dados de navegação e compras dos usuários do e-commerce permitiu compreender melhor o comportamento dos clientes e identificar padrões diretamente relacionados à geração de receita.

# **1. Perfil Geral dos Usuários**

# Os usuários acessam a plataforma em média 25,86 vezes por mês, permanecendo cerca de 32,78 minutos no site por sessão. Cada cliente adiciona, em média, 7,20 itens ao carrinho e realiza compras com ticket médio de R$ 252,70. 

# A mediana do valor gasto é de R$ 248,13. 

# Isso indica que metade dos clientes compra abaixo e metade acima desse valor. Observou-se uma dispersão considerável nos gastos (desvio padrão de R$ 106,94). As compras variam de 23,42 (mínimo) a 530,37 (máximo registrado).

# Esses números mostram que existe um grupo expressivo de consumidores que gasta significativamente mais que a média, mas também há grande variação no comportamento de compra.

# **2. Clientes de Alto Valor**

# Ao analisar os clientes que gastam mais de R$ 250, identificou-se um total de 245 usuários, representando aproximadamente metade da base analisada. Este grupo se destaca por visitar mais vezes o site (33,29 visitas em média) e permanecer por mais tempo (37,11 minutos), comparado ao perfil geral.
# <!-- Trabalho Desenvolvido no Curso da Data Science Academy - www.datascienceacademy.com.br -->
# Isso sugere que engajamento elevado, tanto em frequência de visitas quanto em tempo de navegação, está fortemente associado a compras de maior valor. Esses clientes podem ser considerados um segmento prioritário para ações de fidelização, programas de recompensa e campanhas personalizadas.

# **3. Visitantes Que Não Compram**

# Foi identificado apenas 1 usuário que navega sem realizar compras. Apesar de representar um caso isolado nesta base, ele visita em média 7 vezes e permanece 14,71 minutos no site. Esse comportamento, mesmo pouco expressivo aqui, ilustra a importância de monitorar usuários engajados que não convertem, pois podem representar oportunidades para campanhas de remarketing, melhorias no processo de checkout ou incentivos específicos para concluir a compra.

# **4. Relações Entre Comportamentos e Receita**

# A matriz de correlação revelou informações valiosas:

# - Itens no Carrinho ↔ Valor da Compra = 1,00 → correlação positiva perfeita; cada item adicional impacta diretamente o valor gasto.

# - Tempo no Site ↔ Itens no Carrinho = 0,60 → correlação moderada; usuários que permanecem mais tempo tendem a adicionar mais itens.

# - Tempo no Site ↔ Valor da Compra = 0,59 → correlação moderada; quanto mais tempo no site, maior tende a ser a compra.

# - Visitas ↔ Valor da Compra = 0,65 → correlação positiva; maior frequência de acessos também contribui para compras maiores.

# Esses resultados confirmam que engajamento do usuário (tempo e visitas) influencia a construção do carrinho e, consequentemente, o valor final da compra. Embora seja necessário confirmar a significância estatística com testes adicionais (p-valor), a força das correlações já orienta decisões estratégicas.

# **5. Conclusões e Recomendações**

# - Segmentação estratégica: os clientes de alto valor apresentam comportamento diferenciado, com maior frequência e tempo de navegação. Esse grupo deve ser alvo de campanhas personalizadas e programas de fidelidade para aumentar retenção e ticket médio.

# - Incentivo à construção de carrinho: como a quantidade de itens é fator determinante no valor gasto, estratégias como recomendações personalizadas, descontos progressivos e combos podem elevar o ticket médio.

# - Aproveitamento de visitantes engajados sem compra: embora pouco representativo aqui, vale investir em remarketing e otimização de UX para reduzir fricções no checkout e converter quem demonstra interesse.

# - Base quantitativa para decisões: a análise estatística mostra que dados simples (visitas, tempo, itens) já oferecem insights poderosos para melhorar campanhas de marketing e decisões de produto, substituindo ações baseadas apenas em intuição.

# Este Mini-Projeto, embora simples, demonstra como o NumPy, com poucas linhas de código, nos permite realizar uma análise estatística poderosa, desde a visão geral até a segmentação e correlação, transformando dados brutos em insights de negócio.
