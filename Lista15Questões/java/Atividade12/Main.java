package Atividade12;

public class Main {
    public static void main(String[] args){
        Produto p1 = new Produto("Soja", 10);
        Produto p2 = new Produto("Milho", 4);

        double valorFinal = funcoes.somaValorProdutos(p1, p2);

        System.out.println(valorFinal);
    }
}