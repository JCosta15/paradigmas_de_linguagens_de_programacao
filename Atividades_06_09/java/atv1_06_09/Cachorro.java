package atv1_06_09;

public class Cachorro extends Animal{

    public Cachorro(String nome, String raca) {
        super(nome, raca);
    }

    @Override
    public void emitir_som(){
        System.out.println("Au Au");
    }
}
