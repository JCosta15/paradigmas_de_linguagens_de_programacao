package Atividade1;

public class Main {
    
    public static void main(String[] args) {
        
        Carro carro1 = new Carro("Nissan", "Skyline", 1998);
        Carro carro2 = new Carro("Audi", "R8", 2022);
        Carro carro3 = new Carro("Chevrolet", "Camaro", 2023);

        carro1.mostrar_detalhes();
        carro2.mostrar_detalhes();
        carro3.mostrar_detalhes();
    }
}
