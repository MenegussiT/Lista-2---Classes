class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        else:
            return False

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def consultarSaldo(self):
        return self.saldo

# Criar uma instância da classe ContaCorrente
conta = ContaCorrente("12345", "João")

# Consultar saldo (deve ser zero)
print("Saldo atual:", conta.consultarSaldo())

# Alterar o nome do correntista
conta.alterarNome("Eloyse")

# Realizar um depósito
conta.deposito(1000)

# Consultar o saldo após o depósito
print("Saldo atual:", conta.consultarSaldo())

# Realizar um saque
conta.saque(500)

# Consultar o saldo após o saque
print("Saldo atual:", conta.consultarSaldo())
