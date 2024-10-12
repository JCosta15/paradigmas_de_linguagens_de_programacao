package main

import "fmt"

type Funcionario interface {
	CalcularSalario()
}

type FuncionarioAssalariado struct{
	nome, cargo string
	salario, valorHoraExtra float64
}

func (f FuncionarioAssalariado) CalcularSalario(horasExtras int) float64 {
	return f.salario + float64(horasExtras) * f.valorHoraExtra
}

type FuncionarioHorista struct{
	nome, cargo string
	valorHora float64
}

func (f FuncionarioHorista) CalcularSalario(horasTrabalhadas int) float64 {
	return  float64(horasTrabalhadas) * f.valorHora
}

func main() {
	fAssalariado := FuncionarioAssalariado{
		nome: "Sandro",
		cargo: "Vendedor",
		salario: 2300,
		valorHoraExtra: 15,
	}

	fHorista := FuncionarioHorista{
		nome: "Miguel",
		cargo: "Cozinheiro",
		valorHora: 9,
	}

	fmt.Println(fAssalariado.CalcularSalario(10))
	fmt.Println(fHorista.CalcularSalario(160))
}