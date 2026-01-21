## 12. Entrada e Saída Padrão

#A forma mais comum de interagir com o usuário é através da entrada (input) de dados pelo teclado e da saída (output) de informações na tela.

### 12.1. Saída de Dados com print()

#Já usamos bastante, mas aqui estão alguns recursos adicionais, como as f-strings.

# Variáveis
nome = "Juliana"
idade = 28
cidade = "Rio de Janeiro"

# Usando f-string (a forma mais moderna e recomendada)
print(f"Olá, meu nome é {nome}, tenho {idade} anos e moro no {cidade}.")

# Formatando números
preco = 49.95678
print(f"O preço do produto é R$ {preco:.2f}") # Formata para 2 casas decimais

### 12.2. Entrada de Dados com input()

#A função input() sempre retorna uma string. Por isso, é comum precisar fazer o type casting.

# Pedindo o nome do usuário (string)
nome_usuario = input("Qual é o seu nome? ")

# Pedindo a idade do usuário (precisa converter para int)
idade_usuario_str = input("Qual é a sua idade? ")
idade_usuario_int = int(idade_usuario_str)

from datetime import date

# Pega o ano corrente na data definida no sistema operacional da sua máquina
ano_atual = date.today().year 

# Processando os dados
ano_nascimento = ano_atual - idade_usuario_int

# Exibindo o resultado
print(f"\nOlá, {nome_usuario}! Bem-vindo(a).")
print(f"Você tem {idade_usuario_int} anos e nasceu aproximadamente em {ano_nascimento}.")