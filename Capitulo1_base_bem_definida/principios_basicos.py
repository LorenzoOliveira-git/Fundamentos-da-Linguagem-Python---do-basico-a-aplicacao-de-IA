#1. Lógica de Programação e Pseudocódigo

# O Que é Lógica de Programação?
#Antes de escrever código em uma linguagem de programação, é fundamental entender a lógica por trás da solução de um problema. Um algoritmo é uma sequência de passos finitos e bem definidos para resolver um problema. O pseudocódigo é uma forma de representar esses passos de maneira informal e próxima da linguagem humana, antes de traduzi-los para Python.

### O Que é Pseudocódigo?
#Pseudocódigo é uma forma de descrever algoritmos usando uma linguagem intermediária entre o português (ou outro idioma natural) e uma linguagem de programação real (como Python, Java, C++).
#Ele não segue regras rígidas de sintaxe, mas utiliza estruturas comuns da programação (como se, então, senão, enquanto, para cada, função, etc.), escritas de maneira simples e legível para humanos.
#A ideia é focar na lógica do algoritmo, sem se preocupar com os detalhes técnicos da linguagem que será usada depois.

#Vejamos um exemplo de Pseudocódigo:

#INÍCIO
#   LEIA nota1
#   LEIA nota2

#   CALCULE media = (nota1 + nota2) / 2

#   ESCREVA "A média do aluno é:", media

#   SE media >= 7.0 ENTÃO
#       ESCREVA "Aluno Aprovado!"
#   SENÃO
#       ESCREVA "Aluno Reprovado."
#FIM

#Tradução para python
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"A média do aluno é {media}")

if media >=7:
    print("Aluno Aprovado")
else:
    print("Aluno Reprovado")

#------------------------------------------------------------------------------------------

# 2. Variáveis: Declaração, Atribuição e Regras de Nomenclatura

#Uma variável é um espaço na memória do computador destinado a armazenar dados. Em Python, a declaração e a atribuição de um valor a uma variável são feitas simultaneamente. Regras de Nomenclatura:
#- Nomes de variáveis devem começar com uma letra ou um underscore (_).
#- Não podem começar com um número.
#- Podem conter apenas caracteres alfanuméricos e underscores (A-z, 0-9 e _).
#- São "case-sensitive" (idade é diferente de Idade).
#- Não pode ter (-) no meio da variável
#A linguagem python é tipada, ou seja, quando você declará uma variável nova, o python vai tipar aquela variável.

nome_completo = "Lorenzo Lima"
idade = 16
altura = 1.76
eh_estudante = True

print(f"Nome: {nome_completo}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura}m")
print(f"É estudante? {eh_estudante}")

#Python é uma linguagem dinamicamente "tipada". Você não precisa declarar o tipo das variáveis ao criá-las, pois Python descobre automaticamente pelo valor atribuído:

x = 10        # tipo int
y1 = 10       # tipo int
y2 = "10"     # tipo str

type(x)
type(y1)
type(y2)

# Podemos somar tipos numéricos
print(x + y1)

# Mas não podemos somar número com string
# print(x + y2)

#Ou seja, Python não "mistura" tipos incompatíveis automaticamente e isso mostra que a linguagem não é fracamente tipada.

# ------------------------------------------------------------------------------------------

# 3. Escopo de Variáveis

#O escopo de uma variável define onde ela pode ser acessada no código.

#- Variáveis Globais: Declaradas fora de qualquer função. Podem ser acessadas de qualquer lugar do código.
#- Variáveis Locais: Declaradas dentro de uma função. Só podem ser acessadas dentro daquela função.

# Variável Global
saudacao = "Olá, mundo!"
nome = "Aluno DSA"

# Função
def minha_funcao_dsa():
    
    # Variável Local
    nome = "Ana"
    print(f"\nDentro da função: {nome}")
    print(f"\nAcessando a variável global de dentro da função: {saudacao}")

minha_funcao_dsa()

print(f"\nFora da função: {saudacao}")
print(f"\nFora da função: {nome}")

#OBS: em alguns casos de resolução de problema com a linguagem, usamos o que chamamos de recursão, que é quando eu chamo dentro de um bloco do método, o próprio método. Porem, em questões operacionais, não é muito indicado pois os loops como while ou for resolvem isso de uma melhor forma

# Função
def minha_funcao_dsa():
    
    # Variável Local
    nome_local = "Ana"
    print(f"\nDentro da função: {nome}")
    print(f"\nAcessando a variável global de dentro da função: {saudacao}")

minha_funcao_dsa()

# Tentar acessar a variável local fora da função resultará em um erro (descomente para ver)
# print(f"Tentando acessar 'nome' fora da função: {nome_local}")

# ------------------------------------------------------------------------------------------

# 4. Tipos de Dados Primitivos

#Estes são os tipos de dados mais básicos em Python.

# Integer (Inteiro)
numero_inteiro = 100
print(f"Valor: {numero_inteiro}, Tipo: {type(numero_inteiro)}")

# Float (Ponto Flutuante)
numero_decimal = 19.99
print(f"Valor: {numero_decimal}, Tipo: {type(numero_decimal)}")

# String (Texto)
texto = "Python é incrível!"
print(f"Valor: '{texto}', Tipo: {type(texto)}")

# Boolean (Booleano)
verdadeiro = True
falso = False
print(f"Valor: {verdadeiro}, Tipo: {type(verdadeiro)}")
print(f"Valor: {falso}, Tipo: {type(falso)}")

#Aqui, começamos a entender um conceito muito importante para o Python, a questão de TUDO dentro dessa linguagem é um objeto, ou seja, até os tipos primitivos são objetos. Eles são objetos respectivos de cada classe.