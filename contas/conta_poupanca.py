from conta_bancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def render_juros(self):
        rendimento = self.saldo * 0.05
        self.saldo += rendimento
        print(f"Juros aplicados: R${rendimento:.2f}")