package main

import "fmt"

func Soma2(n1 int, n2 int) int{
	return n1 + n2
}

func Soma3(n1 int, n2 int, n3 int) int{
	return n1 + n2 + n3
}

func main(){
	fmt.Println(Soma2(6, 3))
	fmt.Println(Soma3(7, 7, 7))
}