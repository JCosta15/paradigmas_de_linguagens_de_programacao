package Atividade11;

public class Main {
    public static void main(String[] args) {
        FuncionarioAssalariado fAssalariado = new FuncionarioAssalariado(
                "Carla", "Atendente", 2300, 10);
        FuncionarioHorista fHorista = new FuncionarioHorista(
                "Henrique", "Faxineiro", 8);

        fAssalariado.calcularSalario(10);
        fHorista.calcularSalario(160);

    }
}