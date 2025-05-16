from conta_bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def sacar(self, valor):
        taxa = 1
        total = valor + taxa
        if total > self.saldo:
            print(f"Saldo insuficiente para sacar R${valor:.2f} + taxa de R${taxa:.2f}")
        else:
            self.saldo -= total
            print(f"Saque de R${valor:.2f} efetuado com taxa de R${taxa:.2f}")