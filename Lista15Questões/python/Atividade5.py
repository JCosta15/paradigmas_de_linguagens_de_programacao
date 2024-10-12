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
        print(f"{self.nome} late")

class Gato(Animal):
    def __init__(self, nome, raca, idade):
        super().__init__(nome, raca, idade, "Gato")

    def emitir_som(self):
        print(f"{self.nome} mia")

class Pato(Animal):
    def __init__(self, nome, raca, idade):
        super().__init__(nome, raca, idade, "Pato")

    def emitir_som(self):
        print(f"{self.nome} grasna")

def emitir_som(animais):
    for animal in animais:
        animal.emitir_som()

def detalhes(animais):
    for animal in animais:
        animal.detalhes()

dog = Cachorro("Caramelo", "Vira lata", 4)
cat = Gato("Garfield", "Persa", 5)
duck = Pato("Lucas", "Desconhecida", 2)

animais = [dog, cat, duck]
emitir_som(animais)
detalhes(animais)