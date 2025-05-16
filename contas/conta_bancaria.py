class ContaBancaria:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito R${valor} efetuado!')
    
    def sacar(self, valor):
        taxa = 1
        total = valor + taxa
        if total > self.saldo:
            print(f"Saldo insuficiente para sacar R${valor:.2f} + taxa de R${taxa:.2f}")
        else:
            self.saldo -= total
            print(f"Saque de R${valor:.2f} efetuado com taxa de R${taxa:.2f}")

    def exibir_saldo(self):
        print('=== SALDO ATUAL ===')
        print(f"Nome: {self.nome} - Saldo R${self.saldo:.2f}")



