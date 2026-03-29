import numpy as np
# O computador é incapaz de fazer sequências aleatórias de números, e o numpy.random.seed tem por objetivo gerar números pseudo-aleatórios.
def generate_data():
    np.random.seed(42)

    num_usuarios = 500

    visitas = np.random.randint(1, 51, size = num_usuarios)

    tempo_no_site = np.random.normal(loc = 20, scale = 5, size = num_usuarios) + (visitas * 0.5)
    tempo_no_site = np.round(tempo_no_site, 2) # Arredondar para 2 casas decimais

    itens_no_carrinho = np.random.randint(0, 8, size = num_usuarios) + (visitas // 10)

    itens_no_carrinho = (itens_no_carrinho + (tempo_no_site // 15)).astype(int)

    valor_compra = (itens_no_carrinho * 35) + np.random.normal(loc = 0, scale = 10, size = num_usuarios)

    valor_compra[itens_no_carrinho == 0] = 0
    valor_compra[valor_compra < 0] = 0 # Corrigir valores negativos que possam surgir
    valor_compra = np.round(valor_compra, 2)

    dados_ecommerce = np.column_stack((visitas, tempo_no_site, itens_no_carrinho, valor_compra))

    print("\nShape da nossa massa de dados:", dados_ecommerce.shape)
    print("\nExemplo dos 5 primeiros usuários (linhas):")
    print("\nColunas: [Visitas, Tempo no Site (min), Itens no Carrinho, Valor da Compra (R$)]\n")
    print(dados_ecommerce[:5])

    return dados_ecommerce