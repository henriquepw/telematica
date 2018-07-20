package test;

import academic.controllers.ClassroomController;
import academic.controllers.DisciplineController;
import academic.controllers.ProfessorController;
import academic.controllers.StudentController;

import java.util.Scanner;

public class Main {
    public static ClassroomController classroomController;
    public static DisciplineController disciplineController;
    public static ProfessorController professorController;
    public static StudentController studentController;

    public static void main(String[] args) {
        classroomController = new ClassroomController();
        disciplineController = new DisciplineController();
        professorController = new ProfessorController();
        studentController = new StudentController();

        menu();
    }

    public static void menu() {
        while (true) {
            switch (options()) {
                case 1:

                    break;
                case 2:

                    break;
                case 3:

                    break;
                case 4:

                    break;
                case 5:

                    break;
                case 6:

                    break;
                case 7:

                    break;

                case 11:

                    break;
                case 22:

                    break;
                case 33:
                    break;
                case 0:
                    System.out.println("Sair");
                default:
                    System.out.println("Comando invalido");
            }
        }

    }

    public static int options() {
        System.out.println("1. Cadastar disciplina");
        System.out.println("2. Cadastar professor");
        System.out.println("3. Matricular aluno em turma");
        System.out.println("4. Cadastar turma");
        System.out.println("5. Remover turma");
        System.out.println("6. Exibir todas as turmas por matricula");
        System.out.println("7. Exibir todas os alunos por professor");

        System.out.println("11. Exibir disciplinas");
        System.out.println("22. Exibir professores");
        System.out.println("33. Exibir turmas");
        System.out.println("0. Sair");

        var s = new Scanner(System.in);
        return s.nextInt();
    }
}
