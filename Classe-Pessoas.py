class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            # A cada ano que a idade for menor que 21, a pessoa cresce 0,5 cm
            self.crescer(anos * 0.5)

    def engordar(self, quilos):
        self.peso += quilos

    def emagrecer(self, quilos):
        self.peso -= quilos

    def crescer(self, centimetros):
        self.altura += centimetros

# Criar uma instância da classe Pessoa
pessoa = Pessoa("Ana Carolina", 23, 55, 152)

# Simular o envelhecimento em 3 anos
pessoa.envelhecer(3)

# Simular o ganho de peso de 5 quilos
pessoa.engordar(5)

# Simular o crescimento de 2 cm (fora do padrão de envelhecimento)
pessoa.crescer(2)

# Exibe os dados inseridos
print(f"Nome: {pessoa.nome}")
print(f"Idade: {pessoa.idade} anos")
print(f"Peso: {pessoa.peso} kg")
print(f"Altura: {pessoa.altura} cm")
