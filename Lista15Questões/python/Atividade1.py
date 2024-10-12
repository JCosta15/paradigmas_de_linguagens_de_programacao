class Carro: 
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

carro1 = Carro("Subaru", "Impreza", 2000)
carro2 = Carro("Lotus", "Emira", 2024)
carro3 = Carro("Nissan", "March", 2011)

carro1.exibir_detalhes()
carro2.exibir_detalhes()
carro3.exibir_detalhes()