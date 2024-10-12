package main

import "fmt"

type Produto struct {
	nome string
	valor float64
}

func SomaValorProdutos(p1 Produto, p2 Produto) float64 {
	return p1.valor + p2.valor
}

func main() {
	p1 := Produto{
		nome: "Macarrão",
		valor: 8.0,
	}

	p2 := Produto{
		nome: "Sal",
		valor: 2.0,
	}

	valorFinal := SomaValorProdutos(p1, p2)

	fmt.Println(valorFinal)
}