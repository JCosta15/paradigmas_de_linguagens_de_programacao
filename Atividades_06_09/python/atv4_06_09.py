class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def ligar(self):
        print("O motor está ligado")

    def desligar(self):
        print("O motor está desligado")

class Pneu:
    def __init__(self, marca, tamanho):
        self.marca = marca
        self.tamanho = tamanho

    def encher(self):
        print("O pneu está cheio")

    def esvaziar(self):
        print("O pneu esta vazio")

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor("Gasolina", 150)
        self.pneu = [Pneu("Michellin", 18) for _ in range(4)]

    def ligar(self):
        self.motor.ligar()
        print("O carro está pronto pra rodar")

    def desligar(self):
        self.motor.desligar()
        print("O carro foi desligado")

    def trocar_pneu(self, indice, novo_pneu):
        self.pneus[indice] = novo_pneu
        print(f"Pneu {indice + 1} trocado.")

carro = Carro("Nissa", "GTR")
carro.ligar()


