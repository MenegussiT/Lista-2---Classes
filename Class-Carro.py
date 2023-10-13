class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def adicionarGasolina(self, litros):
        self.combustivel += litros

    def andar(self, distancia):
        consumo_total = distancia / self.consumo
        if self.combustivel >= consumo_total:
            self.combustivel -= consumo_total
        else:
            print("Combustível insuficiente. Não é possível percorrer a distância desejada.")

    def obterGasolina(self):
        return self.combustivel

# Exemplo de uso
meuFusca = Carro(15)  # 15 km por litro de combustível
meuFusca.adicionarGasolina(20)  # Abastece com 20 litros de combustível
meuFusca.andar(100)  # Anda 100 quilômetros
print(f"Combustível restante: {meuFusca.obterGasolina()} litros")
