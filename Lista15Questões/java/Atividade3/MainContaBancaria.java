package Atividade3;

public class MainContaBancaria {
    public static void main(String[] args){
        ContaBancaria conta = new ContaBancaria("Josemar");
        conta.exibir_detalhes();
        conta.depositar(500);
        conta.sacar(300);
        conta.sacar(300);
        conta.exibir_detalhes();
    }
}
