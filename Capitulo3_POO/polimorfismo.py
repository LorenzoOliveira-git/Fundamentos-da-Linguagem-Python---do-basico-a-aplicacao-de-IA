# 5. Fundamentos de POO - Polimorfismo

#Polimorfismo significa "muitas formas". Em POO, refere-se à capacidade de um método se comportar de maneiras diferentes para diferentes objetos. Um exemplo clássico é quando classes filhas sobrescrevem (redefinem) um método da classe pai.

#Vamos criar um método exibir_detalhes na classe Veiculo e sobrescrevê-lo nas classes filhas.

# Cria a Superclasse
class Veiculo:
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_detalhes(self):
        print(f"Veículo genérico: {self.marca} {self.modelo}")

# Cria a Subclasse
class Carro(Veiculo):
    
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    # Sobrescrevendo o método da classe pai
    def exibir_detalhes(self):
        print(f"Carro: {self.marca} {self.modelo} | Portas: {self.portas}")

# Cria a Subclasse
class Moto(Veiculo):
    
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    # Sobrescrevendo o método da classe pai
    def exibir_detalhes(self):
        print(f"Moto: {self.marca} {self.modelo} | Cilindradas: {self.cilindradas}cc")


# Lista de veículos de diferentes tipos
veiculos = [
    Carro("Toyota", "Corolla", 4),
    Moto("Yamaha", "MT-07", 700),
    Veiculo("Caloi", "Ceci")        # Usando a classe pai diretamente
]

# O mesmo método se comporta de forma diferente para cada objeto
for v in veiculos:
    v.exibir_detalhes() # Polimorfismo em ação!