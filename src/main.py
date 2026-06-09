from cliente import Cliente
from banco import Banco
from conta_bancaria import ContaBancaria


banco = Banco("Banco IFAL", 1001)


cliente1 = Cliente(
    "Joao Silva",
    "12345678901",
    "82999999999",
    "joao@email.com"
)

cliente2 = Cliente(
    "Maria Souza",
    "98765432100",
    "82988888888",
    "maria@email.com"
)

cliente3 = Cliente(
    "Pedro Santos",
    "11122233344",
    "82977777777",
    "pedro@email.com"
)


conta1 = ContaBancaria(
    1,
    cliente1,
    banco,
    1000
)

conta2 = ContaBancaria(
    2,
    cliente2,
    banco,
    500
)

conta3 = ContaBancaria(
    3,
    cliente3,
    banco,
    800
)

conta4 = ContaBancaria(
    4,
    cliente1,
    banco,
    300
)


banco.adicionarConta(conta1)
banco.adicionarConta(conta2)
banco.adicionarConta(conta3)
banco.adicionarConta(conta4)


conta1.depositar(200)
conta2.depositar(100)
conta3.depositar(300)


conta1.sacar(150)
conta2.sacar(50)
conta4.sacar(100)


print("Saldo Conta 1:", conta1.consultarSaldo())
print("Saldo Conta 2:", conta2.consultarSaldo())
print("Saldo Conta 3:", conta3.consultarSaldo())
print("Saldo Conta 4:", conta4.consultarSaldo())

###################################

print()
print("===== RELATORIO FINAL =====")
print()

print("Nome do Banco:", banco.nome)
print("Codigo do Banco:", banco.codigo)

print()
print("Quantidade de contas:", banco.quantidadeContas())

saldo_total = 0

print()
print("===== CONTAS CADASTRADAS =====")
print()

for conta in banco.listarContas():

    cliente = conta.getTitular()

    print("Cliente:", cliente.getNome())
    print("CPF:", cliente.getCpf())
    print("Telefone:", cliente.getTelefone())
    print("Email:", cliente.getEmail())

    print("Numero da Conta:", conta.getNumero())
    print("Saldo:", conta.consultarSaldo())

    print()

    saldo_total += conta.consultarSaldo()

print("Saldo Total do Banco:", saldo_total)
