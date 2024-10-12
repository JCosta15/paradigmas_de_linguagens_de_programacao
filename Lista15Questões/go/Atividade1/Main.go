package main

import "fmt"

type Carro struct {
	Marca, Modelo string
	Ano int
}

func (c Carro) exibir_detalhes(){
	fmt.Printf("Marca: %s, Modelo: %s, Ano: %d\n", c.Marca, c.Modelo, c.Ano)
}

func main(){
	
	carro1 := Carro{
		Marca: "Nissan",
		Modelo: "GTR",
		Ano: 2024,
	}
	
	carro2 := Carro{
		Marca: "Mitsubishi",
		Modelo: "Lancer",
		Ano: 2016,
	}
	
	carro3 := Carro{
		Marca: "Porsche",
		Modelo: "Cayman",
		Ano: 2023,
	}

	carro1.exibir_detalhes()
	carro2.exibir_detalhes()
	carro3.exibir_detalhes()
}