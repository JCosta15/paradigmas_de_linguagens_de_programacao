package Atividade4;

public class MainAnimal {
    public static void main(String[] args) {
        Cachorro dog = new Cachorro("Caramelo", "Vira lata", 10);
        Gato cat = new Gato("Garfield", "Persa", 10);

        dog.detalhes();
        cat.detalhes();
        dog.emitir_som();
        cat.emitir_som();
    }
}
