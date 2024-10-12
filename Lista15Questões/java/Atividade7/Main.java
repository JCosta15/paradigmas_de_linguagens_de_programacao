package Atividade7;

public class Main {
    public static void AssociarProfessorEscola(Escola escola, Professor professor) {
        escola.addProfessor(professor);
        professor.addEscola(escola);
    }

    public static void main(String[] args) {
        Professor p1 = new Professor("Mauricio", "234514689");
        Professor p2 = new Professor("Mizael", "234232343");
        Professor p3 = new Professor("Rafael", "245671239");

        Escola e1 = new Escola("Escola1", "9843573592");
        Escola e2 = new Escola("Escola2", "0102345978");
        Escola e3 = new Escola("Escola3", "2213478901");

        AssociarProfessorEscola(e1, p1);
        AssociarProfessorEscola(e1, p2);
        AssociarProfessorEscola(e1, p3);
        AssociarProfessorEscola(e2, p1);
        AssociarProfessorEscola(e2, p2);
        AssociarProfessorEscola(e3, p1);

        p1.detalhesProfessor();
        p2.detalhesProfessor();
        p3.detalhesProfessor();

        e1.detalhesEscola();
        e2.detalhesEscola();
        e3.detalhesEscola();

    }
}