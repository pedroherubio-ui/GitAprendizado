class Carro:
    def __init__(self, Cor, Marca, Ano):
        self.cor = Cor
        self.marca = Marca
        self.ano = Ano
        self.desligado = True
        self.ligado = False

    
    def ligar(self):
        if self.ligado:
            print("Carro já está ligado")
        else:
            print("Carro Ligado")
            self.ligado = True
    
    def desligar(self):
        if self.desligado:
            print("Seu beberrão ja ta desligado")
        else:
            print("Beberrin desligado")
            self.desligado = True