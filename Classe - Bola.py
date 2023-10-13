'''
ECA 2023.2 - Linguagem de programação - Prof: Claudio Miceli

Lista 2 - Exercicio de classe 

'''

class bola:
    def __init__(self, cor, circ, material):
        self.cor = cor
        self.circ= circ
        self.material=material

    def trocar_cor(self, nova_cor):
        self.cor=nova_cor

    def mostrar_cor(self):
        return self.cor

#Criação de instância:
Bola_do_Quico=bola("Azul",30,"couro")

#Mostra cor da bola
print('Cor da bola:', Bola_do_Quico.mostrar_cor())

#trocar cor da bola
Bola_do_Quico.trocar_cor("Verde")

#Mostra a nova cor da bola
print('Nova Cor da bola:', Bola_do_Quico.mostrar_cor())