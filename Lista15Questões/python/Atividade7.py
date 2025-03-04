class Professor:
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf
        self._escolas = []

    def addEscola(self, escola):
        self._escolas.append(escola)
    
    def getNome(self):
        return self._nome
    
    def getCpf(self):
        return self._cpf
    
    def detalhesProfessor(self):
        print("Nome:", self._nome, 
              "\nCPF:", self._cpf,
              "\nEscolas que trabalha:")
        for escola in self._escolas:
            print(f" -Nome: {escola.getNome()}, CNPJ: {escola.getCnpj()}")
        print()


class Escola:
    def __init__(self, nome, cnpj):
        self._nome = nome
        self._cnpj = cnpj
        self._professores = []

    def addProfessor(self, professor):
        self._professores.append(professor)
    
    def getNome(self):
        return self._nome
    
    def getCnpj(self):
        return self._cnpj
    
    def detalhesEscola(self):
        print("Nome:", self._nome, 
              "\nCNPJ:", self._cnpj,
              "\nProfessores que atuam na escola:")
        
        for professor in self._professores:
            print(f" -Nome: {professor.getNome()}, CPF: {professor.getCpf()}")
        
        print()


def associarEscolaProfessor(escola, professor):
    escola.addProfessor(professor)
    professor.addEscola(escola)


p1 = Professor("Julio", "2412561290")
p2 = Professor("Pablo", "2651829401")
p3 = Professor("Romulo", "2221267891")

e1 = Escola("Escola 1", "777212349")
e2 = Escola("Escola 2", "999201234")
e3 = Escola("Escola 3", "212345671")

associarEscolaProfessor(e1, p1)
associarEscolaProfessor(e1, p2)
associarEscolaProfessor(e1, p3)
associarEscolaProfessor(e2, p1)
associarEscolaProfessor(e2, p2)
associarEscolaProfessor(e3, p1)

p1.detalhesProfessor()
p2.detalhesProfessor()
p3.detalhesProfessor()

e1.detalhesEscola()
e2.detalhesEscola()
e3.detalhesEscola()