class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarLados(self, novo_ladoA, novo_ladoB):
        self.ladoA = novo_ladoA
        self.ladoB = novo_ladoB

    def retornarLados(self):
        return self.ladoA, self.ladoB

    def calcularArea(self):
        return self.ladoA * self.ladoB

    def calcularPerimetro(self):
        return 2 * (self.ladoA + self.ladoB)

def calcular_pisos_rodapes(local, piso_area, rodape_comprimento):
    area_local = local.calcularArea()
    perimetro_local = local.calcularPerimetro()

    qtd_pisos = area_local / piso_area
    qtd_rodapes = perimetro_local / rodape_comprimento

    return qtd_pisos, qtd_rodapes

# Função para obter uma valor válido
def obter_float_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= 0:
                return valor
            else:
                print("O valor deve ser positivo.")
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

# Solicitar as medidas do local ao usuário com validação
print("Digite as medidas do local:")
comprimento = obter_float_positivo("Comprimento: ")
largura = obter_float_positivo("Largura: ")

# Criar um objeto Retangulo com as medidas informadas
local = Retangulo(comprimento, largura)

# Solicitar as medidas do piso e do rodapé ao usuário com validação
print("\nDigite as medidas do piso e do rodapé:")
piso_area = obter_float_positivo("Área de cada piso: ")
rodape_comprimento = obter_float_positivo("Comprimento de cada rodapé: ")

# Calcular a quantidade de pisos e rodapés necessários
qtd_pisos, qtd_rodapes = calcular_pisos_rodapes(local, piso_area, rodape_comprimento)

# Exibir os resultados
print("\nResultados:")
print(f"Área do local: {local.calcularArea()} metros quadrados")
print(f"Perímetro do local: {local.calcularPerimetro()} metros")
print(f"Quantidade de pisos necessários: {qtd_pisos:.2f}")
print(f"Quantidade de rodapés necessários: {qtd_rodapes:.2f}")
