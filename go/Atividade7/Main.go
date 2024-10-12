package main

import "fmt"

type Professor struct {
	nome,cpf string
	escolas []Escola
}

func (p *Professor) AddEscola(escola Escola) {
	p.escolas = append(p.escolas, escola)
}

func (p Professor) GetNome() string {
	return p.nome
}

func (p Professor) GetCpf() string {
	return p.cpf
}

func (p Professor) DetalhesProfessor() {
	fmt.Println("Nome: " + p.nome +
	"\nCPF: " + p.cpf +
	"\nEscolas que atua:")
	for _, escola := range p.escolas{
		fmt.Println("  Nome: " + escola.GetNome() + ", CNPJ: " + escola.GetCnpj())
	}
}

type Escola struct {
    nome, cnpj string
	professores []Professor
}

func (e *Escola) AddProfessor(professor Professor) {
	e.professores = append(e.professores, professor)
}

func (e Escola) GetNome() string {
	return e.nome
}

func (e Escola) GetCnpj() string {
	return e.cnpj
}

func (e Escola) DetalhesEscola() {
	fmt.Println("Nome: " + e.nome +
	"\nCNPJ: " + e.cnpj +
	"\nProfessores que atuam na escola:")
	for _, professor := range e.professores{
		fmt.Println("  Nome: " + professor.GetNome() + ", CPF: " + professor.GetCpf())
	}
}

func AssociarEscolaProfessor(escola *Escola, professor *Professor) {
	escola.AddProfessor(*professor)
	professor.AddEscola(*escola)
}

func main() {
	p1 := Professor{
		nome: "Rodrigo",
		cpf: "24567214",
	}

	p2 := Professor{
		nome: "Matheus",
		cpf: "23685912",
	}

	p3 := Professor{
		nome: "Leonardo",
		cpf: "44421679",
	}

	e1 := Escola{
		nome: "Escola1",
		cnpj: "222145760",
	}

	e2 := Escola{
		nome: "Escola2",
		cnpj: "127634520",
	}

    e3 := Escola{
		nome: "Escola3",
		cnpj: "222167490",
	}

	AssociarEscolaProfessor(&e1, &p1)
	AssociarEscolaProfessor(&e1, &p2)
	AssociarEscolaProfessor(&e1, &p3)
	AssociarEscolaProfessor(&e2, &p1)
	AssociarEscolaProfessor(&e2, &p2)
	AssociarEscolaProfessor(&e3, &p1)

	p1.DetalhesProfessor()
	p2.DetalhesProfessor()
	p3.DetalhesProfessor()

	e1.DetalhesEscola()
	e2.DetalhesEscola()
	e3.DetalhesEscola()

}