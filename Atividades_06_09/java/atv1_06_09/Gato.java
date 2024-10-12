package atv1_06_09;

public class Gato extends Animal{

    public Gato(String nome, String raca){
        super(nome,raca);
    }

    @Override
    public void emitir_som(){
        System.out.println("Miau");
    }
}
