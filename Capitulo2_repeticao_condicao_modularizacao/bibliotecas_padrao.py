## 9. Módulos da Biblioteca Padrão Python

#Python vem com uma vasta biblioteca de módulos para todo tipo de tarefa. E se precisar de mais, visite o repositório oficial de pacotes da linguagem:

#https://pypi.org

# Usando o módulo 'math' para funções matemáticas
import math

# Calcula a raiz quadrada
raiz_quadrada = math.sqrt(25)
print(f"A raiz quadrada de 25 é: {raiz_quadrada}")

# Usando o módulo 'random' para gerar números aleatórios
import random

# Gera um inteiro entre 1 e 100
numero_aleatorio = random.randint(1, 100) 
print(f"Um número aleatório entre 1 e 100: {numero_aleatorio}")

# Seleciona aleatoriamente uma cidade da lista
cidade_aleatoria = random.choice(["Rio de Janeiro", "Salvador", "Curitiba"])
print(f"Cidade escolhida aleatoriamente: {cidade_aleatoria}")

#---------------------------------------------------------------------------------------------

## 10. Criando e Importando Seus Próprios Módulos

#Você pode organizar seu código em arquivos (módulos) e importá-los em outros scripts.

# Passo 1: Crie o arquivo do módulo.

#writefile modulodsa.py
"""
    def dsa_saudacao(nome):
        Retorna uma saudação personalizada.
        return f"Olá, {nome}! Tudo bem?"

    PI = 3.14159 """

# Passo 2: Crie o script principal para importar o módulo.

#writefile dsaprincipal.py
"""
    # Conteúdo do arquivo dsaprincipal.py

    # Importa o módulo inteiro
    import modulodsa

    # Usa a função e a variável do módulo
    mensagem = modulodsa.dsa_saudacao("Mundo")
    print(mensagem)
    print(f"O valor de PI do nosso módulo é: {modulodsa.PI}")

    # Outra forma: importando itens específicos
    from modulodsa import dsa_saudacao, PI

    mensagem_direta = dsa_saudacao("Aluno DSA")
    print(mensagem_direta)
    print(f"Valor de PI importado diretamente: {PI}")
"""

#Para executar, você rodaria o arquivo principal.py. O Python automaticamente encontraria e usaria o conteúdo de meu_modulo.py.

#import dsaprincipal