class Animal:
    def __init__(self, nome, raca, idade, especie):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.especie = especie

    def emitir_som(self):
        pass

    def detalhes(self):
        print(f"Nome: {self.nome}, Espécie: {self.especie}, Raça: {self.raca}, Idade: {self.idade}")

class Cachorro(Animal):
    def __init__(self, nome, raca, idade):
        super().__init__(nome, raca, idade, "Cachorro")

    def emitir_som(self):
        print(f"{self.nome} latiu")

class Gato(Animal):
    def __init__(self, nome, raca, idade):
        super().__init__(nome, raca, idade, "Gato")

    def emitir_som(self):
        print(f"{self.nome} miou")

dog = Cachorro("Caramelo", "Vira lata", 10)
cat = Gato("Garfield", "Persa", 11)

dog.emitir_som()
cat.emitir_som()
dog.detalhes()
cat.detalhes()