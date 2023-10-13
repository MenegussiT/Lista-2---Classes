class TV:
    def __init__(self):
        self.ligada = False
        self.canal = 1
        self.volume = 10

    def ligar_desligar(self):
        self.ligada = not self.ligada

    def alterar_canal(self, novo_canal):
        if self.ligada and 1 <= novo_canal <= 100:
            self.canal = novo_canal
        else:
            print("A TV está desligada ou o canal é inválido.")

    def aumentar_volume(self):
        if self.ligada and self.volume < 100:
            self.volume += 1

    def diminuir_volume(self):
        if self.ligada and self.volume > 0:
            self.volume -= 1

    def mostrar_status(self):
        estado = "ligada" if self.ligada else "desligada"
        print(f"TV {estado} | Canal: {self.canal} | Volume: {self.volume}")

# Criar uma instância da classe TV
tv = TV()

# Mostrar o status inicial
tv.mostrar_status()

# Ligar a TV
tv.ligar_desligar()

# Mudar para o canal 50
tv.alterar_canal(45)

# Aumentar o volume
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()

# Mostrar o status atual
tv.mostrar_status()
