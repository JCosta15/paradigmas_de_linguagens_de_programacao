package Atividade15;

public class main {
    public static void main(String[] args){
        ContaBancaria conta = new ContaBancaria("Josemar");
        conta.depositar(500);
        conta.sacar(300);
        conta.sacar(300);
    }
}