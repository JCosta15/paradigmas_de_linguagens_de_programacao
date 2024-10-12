class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura
    
    def calcular_perimetro(self):
        return 2 * (self.comprimento + self.largura)
    
ret = Retangulo(200, 300)
print(f"Área: {ret.calcular_area()}m²")
print(f"Perímetro: {ret.calcular_perimetro()}m")