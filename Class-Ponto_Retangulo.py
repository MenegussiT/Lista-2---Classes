class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Ponto({self.x}, {self.y})")

class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self):
        x = self.ponto_inicial.x + self.largura / 2
        y = self.ponto_inicial.y + self.altura / 2
        return Ponto(x, y)

# Função para alterar os valores do retângulo
def alterar_retangulo(retangulo):
    largura = float(input("Nova largura do retângulo: "))
    altura = float(input("Nova altura do retângulo: "))
    retangulo.largura = largura
    retangulo.altura = altura

# Menu interativo
def menu():
    ponto_inicial = Ponto(0, 0)
    retangulo = Retangulo(ponto_inicial, 4, 3)

    while True:
        print("\nMENU:")
        print("1. Alterar valores do retângulo")
        print("2. Mostrar centro do retângulo")
        print("3. Sair")
        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            alterar_retangulo(retangulo)
        elif escolha == 2:
            centro = retangulo.encontrar_centro()
            centro.imprimir()
        elif escolha == 3:
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
