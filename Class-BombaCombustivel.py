class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            return litros_abastecidos
        else:
            litros_abastecidos = self.quantidade_combustivel
            self.quantidade_combustivel = 0
            return litros_abastecidos

    def abastecer_por_litro(self, litros):
        if litros <= self.quantidade_combustivel:
            valor_a_pagar = litros * self.valor_litro
            self.quantidade_combustivel -= litros
            return valor_a_pagar
        else:
            return 0  # Não há combustível suficiente na bomba.

    def alterar_valor(self, novo_valor_litro):
        self.valor_litro = novo_valor_litro

    def alterar_combustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel

    def alterar_quantidade_combustivel(self, nova_quantidade_combustivel):
        self.quantidade_combustivel = nova_quantidade_combustivel

    def mostrar_estado(self):
        print(f"Tipo de Combustível: {self.tipo_combustivel}")
        print(f"Valor por Litro: R${self.valor_litro:.2f}")
        print(f"Quantidade de Combustível na Bomba: {self.quantidade_combustivel:.2f} litros")

# Criar uma instância da bomba de combustível
bomba = BombaCombustivel("Gasolina", 4.50, 1000.0)

while True:
    print("\nMENU:")
    print("1. Abastecer por valor")
    print("2. Abastecer por litro")
    print("3. Alterar valor do litro")
    print("4. Alterar tipo de combustível")
    print("5. Alterar quantidade de combustível na bomba")
    print("6. Mostrar estado da bomba")
    print("7. Sair")
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        valor_abastecido = float(input("Informe o valor a ser abastecido: R$"))
        litros_abastecidos = bomba.abastecer_por_valor(valor_abastecido)
        if litros_abastecidos > 0:
            print(f"Foram abastecidos {litros_abastecidos:.2f} litros.")
        else:
            print("Não há combustível suficiente na bomba.")
    elif escolha == 2:
        litros_abastecer = float(input("Informe a quantidade de litros a abastecer: "))
        valor_a_pagar = bomba.abastecer_por_litro(litros_abastecer)
        if valor_a_pagar > 0:
            print(f"O cliente deve pagar R${valor_a_pagar:.2f}.")
        else:
            print("Não há combustível suficiente na bomba.")
    elif escolha == 3:
        novo_valor_litro = float(input("Informe o novo valor por litro: R$"))
        bomba.alterar_valor(novo_valor_litro)
    elif escolha == 4:
        novo_tipo_combustivel = input("Informe o novo tipo de combustível: ")
        bomba.alterar_combustivel(novo_tipo_combustivel)
    elif escolha == 5:
        nova_quantidade_combustivel = float(input("Informe a nova quantidade de combustível na bomba: "))
        bomba.alterar_quantidade_combustivel(nova_quantidade_combustivel)
    elif escolha == 6:
        bomba.mostrar_estado()
    elif escolha == 7:
        break
    else:
        print("Opção inválida. Tente novamente.")
