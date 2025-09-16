class Computador:
    def __init__(self, cpu, gpu, gab, font, mae):
        self.cpu = cpu
        self.gpu = gpu
        self.gab = gab
        self.font = font
        self.mae = mae
        self.desligado = True
        self.ligado = False
        

    def ligar(self):
        if self.ligado:
            print("Seu PC ja está ligado")
        else:
            print("Computador ligado")
            self.ligado = True

    def desligar(self):
        if self.desligado:
            print("Seu PC ja esta desligado")
        else:
            print("PC desligado")

