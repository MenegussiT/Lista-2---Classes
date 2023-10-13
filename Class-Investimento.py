class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def obter_saldo(self):
        return self.saldo

class ContaInvestimento(ContaBancaria):
    def __init__(self, saldo_inicial, taxa_juros):
        super().__init__(saldo_inicial)
        self.taxa_juros = taxa_juros

    def adicione_juros(self):
        juros = self.saldo * (self.taxa_juros / 100)
        self.deposito(juros)

# Criar uma conta de investimento com saldo inicial de R$1000,00 e taxa de juros de 10%
minha_conta_investimento = ContaInvestimento(1000, 10)

# Aplicar o método adicioneJuros cinco vezes
for _ in range(5):
    minha_conta_investimento.adicione_juros()

# Imprimir o saldo resultante
saldo_final = minha_conta_investimento.obter_saldo()
print(f"Saldo resultante após aplicar juros: R${saldo_final:.2f}")
