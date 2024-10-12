package Atividade6;

public class Main {
    public static void main(String[] args) {
        Motor motor = new Motor("Flex", 2000);
        Carro carro = new Carro("Renault", "Kwid", 2022, motor);

        System.out.println(carro.detalhesCarro());
    }
}