class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        return self.bucho

    def digerir(self):
        if self.bucho:
            self.bucho.clear()
            print(f"{self.nome} digeriu a comida.")
        else:
            print(f"{self.nome} não tem nada no estômago.")

# Criar dois macacos
macaco1 = Macaco("Macaco A")
macaco2 = Macaco("Macaco B")

# Alimentar o primeiro macaco com o segundo macaco (ficção)
macaco1.comer(macaco2)

# Verificar o conteúdo do estômago do primeiro macaco
print(f"Conteúdo do estômago de {macaco1.nome}: {macaco1.verBucho()}")
