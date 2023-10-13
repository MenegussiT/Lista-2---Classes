class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obter_nome(self):
        return self.nome

    def obter_salario(self):
        return self.salario

    def aumentar_salario(self, porcentagem_de_aumento):
        aumento = self.salario * (porcentagem_de_aumento / 100)
        self.salario += aumento

# Exemplo de uso
harry = Funcionario("Harry", 25000)
print(f"Salário inicial de {harry.obter_nome()}: R${harry.obter_salario():.2f}")

harry.aumentar_salario(10)  # Aumentar o salário em 10%
print(f"Novo salário de {harry.obter_nome()}: R${harry.obter_salario():.2f}")
