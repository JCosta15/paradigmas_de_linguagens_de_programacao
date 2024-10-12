class Motor:
    def __init__(self, tipo, cilindradas):
        self.tipo = tipo
        self.cilindradas = cilindradas

    def detalhesMotor(self):
        return f"{self.tipo} de {self.cilindradas} cilindradas"

class Carro:
    def __init__(self, marca, modelo, ano, motor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.motor = motor

    def detalhesCarro(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Motor: {self.motor.detalhesMotor()}"

carro = Carro("Bugatti", "Chiron", 2024, Motor("Híbrido", 10000))

print(carro.detalhesCarro())