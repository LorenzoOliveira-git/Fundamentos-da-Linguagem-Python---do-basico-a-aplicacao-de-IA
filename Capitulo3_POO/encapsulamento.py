# 3. Fundamentos de POO - Encapsulamento

#O encapsulamento é a ideia de agrupar os dados (atributos) e os métodos que operam nesses dados dentro de uma única unidade (a classe). Ele também envolve restringir o acesso direto aos atributos, geralmente usando um _ (protegido) ou __ (privado) no início do nome do atributo. O acesso é feito através de métodos (getters e setters), o que dá mais controle sobre como os dados são modificados.

#Vamos modificar a classe Carro para encapsular velocidade e horsepower.

class Carro:

    def __init__(self, marca, modelo, ano):

        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self._velocidade = 0
        self.__horsepower = 300

    # Método "getter" para obter o valor da velocidade
    def get_velocidade(self):
        return self._velocidade
    
    # Método "setter" para alterar o valor da velocidade com lógica de controle
    def acelerar(self, valor):
        if valor > 0:
            self._velocidade += valor
            print(f"O {self.modelo} acelerou para {self._velocidade} Km/h.")
        else:
            print("O valor de aceleração tem que ser positivo.")

    # Método geral
    def frear(self, valor):
        if valor > 0:
            self._velocidade -= valor
            if self._velocidade < 0:
                self._velocidade = 0
            print(f"O {self.modelo} freou para {self._velocidade} Km/h.")
        else:
            print("O valor de frenagem deve ser positivo.")

# Cria a instância da classe
carro_encapsulado = Carro("Hyundai", "HB20", 2026)

# Observe que o atributo _velocidade não aparece na lista
carro_encapsulado.ano

# Interagindo com o objeto através de métodos
carro_encapsulado.acelerar(50)
print(f"Velocidade atual: {carro_encapsulado.get_velocidade()} km/h")
carro_encapsulado.frear(20)
print(f"Velocidade atual: {carro_encapsulado.get_velocidade()} km/h")

# Conseguimos acessar diretamente o atributo protegido
print(carro_encapsulado._velocidade)

# Acesso direto (não recomendado)
carro_encapsulado._velocidade = 200 # Isso quebra o encapsulamento!
print(f"Velocidade alterada diretamente: {carro_encapsulado._velocidade} km/h")

#**ATENÇÃO**: A célula acima funciona porque, em Python, o uso de um único sublinhado no início de um atributo (como _velocidade) é apenas uma convenção de programação, não uma regra imposta pela linguagem. Ou seja, o sublinhado indica para outros desenvolvedores que aquele atributo é considerado "protegido" e não deve ser acessado diretamente fora da classe, mas o interpretador Python não impede que você o modifique. Python aceita normalmente, sobrescrevendo o valor interno do atributo, mesmo que isso quebre a lógica de encapsulamento. Diferente de linguagens como Java ou C++, onde o modificador private de fato impede o acesso externo, em Python a proteção é baseada em boas práticas e disciplina do programador.

#Se a intenção fosse dificultar ainda mais o acesso direto, poderia ser usado duplo sublinhado (__horsepower), que aciona um processo chamado name mangling. Isso não torna o atributo verdadeiramente privado, mas altera o nome interno e dificulta acessá-lo acidentalmente, embora ainda seja possível com alguma insistência.

# Tentativa de acesso direto falha
try:
    print(carro_encapsulado.__horsepower)
except AttributeError as e:
    print("Erro ao acessar diretamente:", e)

# Mas o atributo existe, só que com nome interno modificado
print("Acessando pelo nome real interno:", carro_encapsulado._Carro__horsepower)

# Acesso direto (não recomendado)
carro_encapsulado.__horsepower = 350   # Isso quebra o encapsulamento!
print(f"Horsepower alterado diretamente: {carro_encapsulado.__horsepower}")

#Resumindo

#- _atributo → apenas convenção, acesso é permitido.

#- __atributo → Python aplica name mangling, mudando o nome interno do atributo para _NomeDaClasse__atributo. Isso dificulta o acesso, mas ainda é possível se você souber o nome interno.

#Ou seja, em Python o encapsulamento é mais cultural do que técnico.
