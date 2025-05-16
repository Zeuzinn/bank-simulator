# Banco
# 💰 Simulador Bancário

Este projeto implementa uma classe simples de conta bancária com funcionalidades básicas como depósito, saque (com taxa) e exibição de saldo.

## 🧾 Funcionalidades

- Criar uma conta com nome do titular.
- Depositar valores na conta.
- Sacar valores (com taxa fixa de R$1).
- Exibir o saldo atual da conta.

## 🧩 Estrutura da Classe

### `ContaBancaria(nome)`

- Inicializa a conta com nome e saldo zerado.

### Métodos disponíveis:

#### `depositar(valor)`
- Adiciona o valor ao saldo da conta.
- Exibe mensagem de confirmação.

#### `sacar(valor)`
- Subtrai o valor do saldo (com taxa de R$1).
- Se o saldo for insuficiente, exibe aviso.

#### `exibir_saldo()`
- Mostra o nome do titular e o saldo atual formatado.

## 🧪 Exemplo de Uso

```python
from conta import ContaBancaria

conta = ContaBancaria("João")
conta.depositar(100)
conta.sacar(30)
conta.exibir_saldo()
