import random

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 100)
        self.tedio = random.randint(0, 100)

    def alimentar(self, quantidade_comida):
        self.fome -= quantidade_comida
        if self.fome < 0:
            self.fome = 0

    def brincar(self, tempo_brincadeira):
        self.tedio -= tempo_brincadeira
        if self.tedio < 0:
            self.tedio = 0

    def humor(self):
        if self.fome > 75 and self.tedio > 75:
            return "Estou entediado e com fome!"
        elif self.fome > 75:
            return "Estou com fome!"
        elif self.tedio > 75:
            return "Estou entediado!"
        else:
            return "Estou feliz"

    def mostrar_atributos(self):
        return f"{self.nome} - Fome: {self.fome}, Tédio: {self.tedio}"

class FazendaDeBichinhos:
    def __init__(self):
        self.bichinhos = []

    def adicionar_bichinho(self, nome):
        bichinho = BichinhoVirtual(nome)
        self.bichinhos.append(bichinho)

    def alimentar_todos(self, quantidade_comida):
        for bichinho in self.bichinhos:
            bichinho.alimentar(quantidade_comida)

    def brincar_todos(self, tempo_brincadeira):
        for bichinho in self.bichinhos:
            bichinho.brincar(tempo_brincadeira)

    def ouvir_todos(self):
        for bichinho in self.bichinhos:
            print(bichinho.humor())

    def listar_bichinhos(self):
        for bichinho in self.bichinhos:
            print(bichinho.mostrar_atributos())

def main():
    fazenda = FazendaDeBichinhos()

    while True:
        print("\nMENU:")
        print("1. Adicionar Bichinho")
        print("2. Alimentar todos os bichinhos")
        print("3. Brincar com todos os bichinhos")
        print("4. Ouvir todos os bichinhos")
        print("5. Mostrar atributos dos bichinhos")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite o nome do novo bichinho: ")
            fazenda.adicionar_bichinho(nome)
        elif escolha == '2':
            comida = int(input("Quanta comida você vai dar? (0 a 100): "))
            fazenda.alimentar_todos(comida)
        elif escolha == '3':
            tempo_brincadeira = int(input("Quanto tempo você vai brincar? (0 a 100): "))
            fazenda.brincar_todos(tempo_brincadeira)
        elif escolha == '4':
            fazenda.ouvir_todos()
        elif escolha == '5':
            fazenda.listar_bichinhos()
        elif escolha == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
