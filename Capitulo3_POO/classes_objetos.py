#2. Classes e Objetos - Abstraindo Entidades do Mundo Real

#Uma Classe é como um "molde" para criar objetos. Ela define um conjunto de atributos (características) e métodos (comportamentos) que os objetos desse tipo terão.

#Um Objeto é uma instância de uma classe. É a entidade real, criada a partir do molde (classe), co# Definindo a Classe (o molde)

class Carro:
    
    # O método __init__ é um "construtor". Ele é chamado quando um novo objeto é criado.
    # 'self' se refere à instância do objeto que está sendo criado. É de extrema importância para o python reconhecer qual instância da classe ele deve armazenar os dados, além de indicar quais dados usar nos métodos da classe.
    def __init__(self, marca, modelo, ano):
        
        # Atributos (dados) do objeto
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False # Um carro começa desligado por padrão

    # Métodos (comportamentos) do objeto
    def ligar(self):
        
        if not self.ligado:
            self.ligado = True
            print(f"O {self.modelo} está ligado.")
        else:
            print(f"O {self.modelo} já estava ligado.")

    def desligar(self):
        
        if self.ligado:
            self.ligado = False
            print(f"O {self.modelo} foi desligado.")
        else:
            print(f"O {self.modelo} já estava desligado.")

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

#Trabalhando com instâncias da classe.

# Criando objeto (instância da classe Carro)
carro_1 = Carro("Volkswagen", "Fusca", 1967)

# Usando os objetos
carro_1.exibir_informacoes()

carro_1.ligar()

carro_1.desligar()

# Criando objeto (instância da classe Carro)
carro_2 = Carro("Tesla", "Model S", 2025)

carro_2.exibir_informacoes()

carro_2.ligar()


