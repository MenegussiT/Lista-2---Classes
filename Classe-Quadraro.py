class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudaLado(self, novo_lado):
        self.tamanho_lado = novo_lado

    def retornaLado(self):
        return self.tamanho_lado

    def calcularArea(self):
        return self.tamanho_lado ** 2
    
# Cria uma instância da classe Quadrado
meu_quadrado = Quadrado(5)

# Retornar o valor do lado do quadrado
print("Tamanho do lado do quadrado:", meu_quadrado.retornaLado())

# Muda o valor do lado do quadrado
meu_quadrado.mudaLado(7)

# Retorna o novo valor do lado do quadrado
print("Novo tamanho do lado do quadrado:", meu_quadrado.retornaLado())

# Calcula a área do quadrado
area = meu_quadrado.calcularArea()
print("Área do quadrado:", area)

