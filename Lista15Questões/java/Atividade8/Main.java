package Atividade8;

public class Main {
    public static void main(String[] args) {
        Empregado e1 = new Empregado("Julio", "Designer", 50000);
        Empregado e2 = new Empregado("Alisson", "Programdos Senior", 15000);
        Empregado e3 = new Empregado("Vitor", "Estagiário", 2500);

        Empresa empresa = new Empresa("Softcom", "23451209851");

        empresa.addEmpregado(e1);
        empresa.addEmpregado(e2);
        empresa.addEmpregado(e3);

        empresa.detalhes();
    }
}
