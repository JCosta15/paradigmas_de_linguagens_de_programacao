class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco
    
    def __add__(self, other):
        return self.__preco + other.__preco

p1 = Produto("Sal", 5)
p2 = Produto("Açucar", 6)

valorFinal = p1 + p2

print(valorFinal)