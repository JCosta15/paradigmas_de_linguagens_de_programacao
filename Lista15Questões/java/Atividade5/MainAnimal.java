package Atividade5;
import java.util.List;

public class MainAnimal {

    public static void emitir_som(List<Animal> animais) {
        for (Animal animal: animais){
            animal.emitir_som();
        }
    }

    public static void detalhes(List<Animal> animais) {
        for (Animal animal: animais){
            animal.detalhes();
        }
    }

    public static void main(String[] args) {
        Cachorro dog = new Cachorro("Caramelo", "Vira lata", 10);
        Gato cat = new Gato("Garfield", "Persa", 10);

        List<Animal> animais = List.of(dog, cat);

        detalhes(animais);
        emitir_som(animais);
    }
}
