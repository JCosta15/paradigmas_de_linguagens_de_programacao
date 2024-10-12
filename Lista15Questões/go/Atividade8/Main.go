package main

import "fmt"

type Empregado struct {
	nome string
    cargo string
    salario float64
}
    
func (e Empregado) Detalhes() {
	fmt.Printf(" -Nome: %s, Cargo: %s, Salário: %.2f\n", e.nome, e.cargo, e.salario)
}
        
type Empresa struct {
	nome, cnpj string
    empregados []Empregado
}
          
func (e *Empresa) addEmpregados(empregado Empregado) {
	e.empregados = append(e.empregados, empregado)
}
            
func (e Empresa) detalhes() {
	
	fmt.Println("Nome:", e.nome,
              "\nCNPJ:", e.cnpj,
              "\nEmpregados:")
        
    for _, empregado := range e.empregados {
		empregado.Detalhes()
	}
               
    fmt.Println()
}        
        
func main() {
	
	e1 := Empregado{
		nome: "Fabiano",
	    cargo: "Programador Senior",
	    salario: 13000,
	}

	e2 := Empregado{
		nome: "Rogerio",
		cargo: "Programador Pleno",
		salario: 7000,
	}

	e3 := Empregado{
		nome: "Lucas",
		cargo: "Faxineiro",
		salario: 2000,
	}

	empresa := Empresa{
		nome: "Amazon",
		cnpj: "221456340",
	}

    empresa.addEmpregados(e1)
    empresa.addEmpregados(e2)
    empresa.addEmpregados(e3)

    empresa.detalhes()
}

