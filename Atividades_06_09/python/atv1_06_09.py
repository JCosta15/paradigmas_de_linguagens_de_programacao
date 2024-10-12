class Animal:
    def __init__(self, especie, nome):
        self.nome = nome
        self.especie = especie

    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au"

class Gato(Animal):
    def emitir_som(self):
        return "Miau"

pet = Cachorro("cachorro","Caramelo")

print(pet.emitir_som())
