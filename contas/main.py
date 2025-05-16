from conta_bancaria import ContaBancaria
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca


conta = ContaBancaria("Eliseu")
conta.exibir_saldo()
conta.depositar(2000)
conta.sacar(325)
print()
conta.exibir_saldo()
print()

conta_2 = ContaCorrente("Robson")
conta_2.exibir_saldo()
conta_2.depositar(1450)
conta_2.sacar(349)
print()
conta_2.exibir_saldo()
print()

conta_3 = ContaPoupanca("Flabeu")
conta_3.exibir_saldo()
conta_3.depositar(1500) 
conta_3.sacar(855)
conta_3.render_juros()
print()
conta_3.exibir_saldo()
print()


help(ContaBancaria)