class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.tedio = 50

    def alimentar(self, quantidade_comida):
        self.fome -= quantidade_comida

    def brincar(self, tempo_brincadeira):
        self.tedio -= tempo_brincadeira

    def humor(self):
        if self.fome > 75 and self.tedio > 75:
            return "Estou entediado e com fome!"
        elif self.fome > 75:
            return "Estou com fome!"
        elif self.tedio > 75:
            return "Estou entediado!"
        else:
            return "Estou feliz!"

    def mostrar_atributos(self):
        return f"{self.nome} - Fome: {self.fome}, Tédio: {self.tedio}"

# Função para interagir com o bichinho virtual
def interagir_com_bichinho(bichinho):
    print(f"Olá, sou {bichinho.nome}! Como posso ajudar você?")
    while True:
        print("\nMENU:")
        print("1. Alimentar o bichinho")
        print("2. Brincar com o bichinho")
        print("3. Verificar humor do bichinho")
        print("4. Opção secreta: Mostrar atributos do bichinho")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            comida = int(input("Quanta comida você vai dar? (0 a 100): "))
            bichinho.alimentar(comida)
        elif escolha == '2':
            tempo_brincadeira = int(input("Quanto tempo você vai brincar? (0 a 100): "))
            bichinho.brincar(tempo_brincadeira)
        elif escolha == '3':
            print(bichinho.humor())
        elif escolha == '4':
            print(bichinho.mostrar_atributos())  # Mostrar os atributos do bichinho (secreto)
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

# Exemplo de uso
nome_bichinho = input("Digite o nome do seu bichinho: ")
meu_bichinho = BichinhoVirtual(nome_bichinho)
interagir_com_bichinho(meu_bichinho)
