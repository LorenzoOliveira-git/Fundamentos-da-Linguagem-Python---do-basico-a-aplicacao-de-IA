#Classe base abstrata e o decarador para métodos abstratos
from abc import ABC, abstractmethod

from datetime import datetime
from Utilitarios.exceptions import SaldoInsuficienteError

#CONTA - classe mãe
class Conta(ABC):
    
    _total_contas = 0

    def __init__(self, numero: int, cliente):

        self._numero = numero
        self._saldo = 0.0
        self._cliente = cliente
        self._historico = []

        Conta._total_contas += 1
    
    #Decorador de função que transforma o saldo em uma propriedade, ou seja, em vez de chama-lo como uma função obj.saldo(), você irá chama-lo como atributo abj.saldo. Isso permite que você leia o atributo protegido, porém não consiga modifica-lo em razão do seu encapsulamento.
    @property
    def saldo(self):
        return self._saldo
    
    #Decorador de função que permite a manipulação de atributos em nível de classe, ou seja, modificar um atributo que não muda dependendo da instância. Nessa caso, o atributo que está em nível de classe é _total_contas, por isso ele não tem a palavra reservada "self" e sim "cls" (class)
    @classmethod
    def getTotalContas(cls):
        return cls._total_contas
    
    def depositar(self, valor: float):
        if valor > 0:
            self._saldo += valor
            self._historico.append((datetime.now(), f"Depósito de R${valor:.2f}"))
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito deve ser maior que zero.")

    #Dentro da POO temos as métodos abstratas, que servem para forçar as classes filhas (herança) a implementarem esse método. Ou seja, toda classe filha terá que ter a sua versão de sacar, neste caso. E esse conceito foi implementado com o decorador de método da biblioteca ABC que indica ao python que aquele método é abstrato.
    @abstractmethod
    def sacar(self, valor: float):
        pass

    def extrato(self):

        print(f"\n--- Extrato da Conta Nº {self._numero} ---")
        print(f"Cliente: {self._cliente.nome}")
        print(f"Saldo atual: R${self._saldo:.2f}")
        print("Histórico de transações:")

        if not self._historico:
            print("Nenhuma transação registrada.")

        for data, transacao in self._historico:
            print(f"- {data.strftime('%d/%m/%Y %H:%M:%S')}: {transacao}")
        print("--------------------------------------\n")

#CONTA CORRENTE - filha
class ContaCorrente(Conta):

    def __init__(self, numero: int, cliente, limite: float = 500.0):
        super().__init__(numero,cliente)
        self.limite = limite

    def sacar(self, valor: float):
        if valor <= 0:
            print("Valor de saque inválido")
            return
        saldo_disponivel = self._saldo + self.limite

        if valor > saldo_disponivel:
            #Raise - palavra reservada em python que serve para criar uma exceção 
            raise SaldoInsuficienteError(saldo_disponivel, valor, "Saldo e limite insuficientes.")
        
        self._saldo -= valor

        self._historico.append((datetime.now(),f"Saque de R${valor:.2f}"))
        print(f"Saque de R${valor:.2f} realizado com sucesso.")

#CONTA POUPANÇA - filha
class ContaPoupanca(Conta):

    def __init__(self, numero: int, cliente):
        super().__init__(numero,cliente)

    def sacar(self, valor: float):
        if valor <= 0:
            print("Valor de saque inválido.")
            return

        if valor > self._saldo:
            raise SaldoInsuficienteError(self._saldo, valor)
        
        self._saldo -= valor

        self._historico.append((datetime.now(),f"Saque de R${valor:.2f}"))
        print(f"Saque de R${valor:.2f} realizado com sucesso.")

