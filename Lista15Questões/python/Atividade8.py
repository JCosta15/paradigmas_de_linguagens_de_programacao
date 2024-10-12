class Empregado:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def detalhes(self):
        print(f" -Nome: {self.nome}, Cargo: {self.cargo}, Salário: {self.salario}")

class Empresa:
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj
        self._empregados = []
    
    def addEmpregados(self, empregado):
        self._empregados.append(empregado)
    
    def detalhes(self):
        
        print("Nome: ", self.nome,
              "\nCNPJ: ", self.cnpj,
              "\nEmpregados:")
        
        for empregado in self._empregados:
            empregado.detalhes()
        
        print()

e1 = Empregado("Vinicius", "Dev Portugol", 30000)
e2 = Empregado("Astolfo", "Programador Senior", 7000)
e3 = Empregado("Junior", "Estagiário", 2500)

empresa = Empresa("Ubisoft", "21245681")

empresa.addEmpregados(e1)
empresa.addEmpregados(e2)
empresa.addEmpregados(e3)

empresa.detalhes()
           