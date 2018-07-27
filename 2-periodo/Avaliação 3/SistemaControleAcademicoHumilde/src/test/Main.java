package test;

import academic.facade.Facade;

import java.util.*;

public class Main {
    public static Facade facade;

    public static void main(String[] args) {
        facade = new Facade();

        facade.registerDiscipline(1, 10, "programacao 2", "Estrutura de dados e poo");
        facade.registerProfessor(2020, "Marcelo");
        facade.registerStudent(2017, "Henrique", "Telematica");
        facade.registerClassroom(101, 1, 2020);
        facade.registerStudentInClass(2017, 101);
        menu();
    }

    public static int getInt() {
        boolean stay = true;
        int inteiro = 0;
        while (stay) {
            try {
                inteiro = new Scanner(System.in).nextInt();
                stay = false;
            } catch (InputMismatchException e) {
                System.out.println("Erro, tente novamente.");
            }
        }
        return inteiro;
    }

    public static int options() {
        System.out.println("1. Cadastar disciplina");
        System.out.println("2. Cadastar professor");
        System.out.println("3. Matricular aluno(s) em turma");
        System.out.println("4. Cadastar turma");
        System.out.println("5. Remover turma");
        System.out.println("6. Exibir todas as turmas por matricula");
        System.out.println("7. Exibir todas os alunos por professor");

        System.out.println("Extras: ");
        System.out.println("8. Cadastar aluno");
        System.out.println("11. Exibir disciplinas");
        System.out.println("22. Exibir professores");
        System.out.println("33. Exibir turmas");
        System.out.println("44. Exibir alunos");
        System.out.println("0. Sair");

        return getInt();
    }

    public static void menu() {
        Scanner s = new Scanner(System.in);
        boolean stay = true;
        while (stay)
            switch (options()) {
                case 1: // Cadastro de Disciplina
                    cadastroDisciplina();
                    break;
                case 2: // Cadastro de Professor
                    cadastroProfessor();
                    break;
                case 3: // Matricular aluno em turma
                    matriculaAlunos();
                    break;
                case 4: // Cadastro de Turma
                    cadastroTurma();
                    break;
                case 5: // Remover turma
                    removeTurma();
                    break;
                case 6: // Exibir todos as classe por aluno
                    exibeTurmasPorAluno();
                    break;
                case 7: //Exibir todos os alunos por professor
                    exibeAlunosPorProfessor();
                    break;
                case 8: // Cadastro de aluno
                    cadastroAluno();
                    break;
                case 11: // Exibir todas as disciplinas
                    System.out.println(facade.getDisciplines().toString());
                    break;
                case 22: // Exibir todas os professores
                    System.out.println(facade.getProfessors().toString());
                    break;
                case 33: // Exibir todas as turmas
                    System.out.println(facade.getClassrooms().toString());
                    break;
                case 44: // Exibir todas os alunos
                    System.out.println(facade.getStudents().toString());
                    break;
                case 0:
                    stay = false;
                    break;
                default:
                    System.out.println("Comando invalido");
            }
    }

    public static void cadastroDisciplina() {
        Scanner sStr = new Scanner(System.in);
        System.out.println("Digite -1 a qualquer momento para cancelar o cadastro.");

        System.out.print("Id: ");
        int id = getInt();
        if (id != -1) {
            System.out.print("Carga horaria: ");
            int hours = getInt();

            if (hours != -1) {
                System.out.print("Nome: ");
                String name = sStr.nextLine();

                if (!name.equals("-1")) {
                    System.out.print("Descricao: ");
                    String description = sStr.nextLine();

                    if (!description.equals("-1"))
                        if (!facade.registerDiscipline(id, hours, name, description))
                            System.out.println("Erro: Disciplina com esse id ja existe");
                        else
                            System.out.println("Cadastro feito com sucesso!");
                }
            }
        }
    }

    public static void cadastroProfessor() {
        Scanner sStr = new Scanner(System.in);
        System.out.println("Digite -1 a qualquer momento para cancelar o cadastro.");

        System.out.print("Nome: ");
        String name = sStr.nextLine();
        if (!name.equals("-1")) {
            System.out.print("Matricula: ");
            int enrollment = getInt();

            if (enrollment != -1)
                if (!facade.registerProfessor(enrollment, name))
                    System.out.println("Erro: Professor com essa matricula ja existe");
                else
                    System.out.println("Cadastro feito com sucesso!");
        }
    }

    public static void cadastroAluno() {
        Scanner s = new Scanner(System.in);
        System.out.println("Digite -1 a qualquer momento para cancelar o cadastro.");

        System.out.print("Nome: ");
        String name = s.nextLine();
        if (!name.equals("-1")) {
            System.out.print("Matricula: ");
            int enrollment = getInt();

            if (enrollment != -1) {
                System.out.print("Curso: ");
                String course = s.nextLine();

                if (!course.equals("-1"))
                    if (!facade.registerStudent(enrollment, name, course))
                        System.out.println("Aluno com esse id ja existe");
                    else
                        System.out.println("Cadastro feito com sucesso!");
            }
        }
    }

    public static void cadastroTurma() {
        int id, disciplineID, professorID;

        if (facade.getDisciplines().size() == 0)
            System.out.println("Cadastre uma disciplina antes de cadastrar uma turma.");
        else if (facade.getProfessors().size() == 0)
            System.out.println("Cadastre um professor antes de cadastrar uma turma.");
        else {
            System.out.println("Digite -1 a qualquer momento para cancelar o cadastro.");

            while (true) {
                System.out.print("Codigo da turma: ");
                id = getInt();
                if (!facade.checkOutClassroom(id) || (id == -1)) break;
                else System.out.println("Turma com esse id ja existe, digite outra.");
            }

            if (id != -1) {
                while (true) {
                    System.out.print("Codigo da disciplina: ");
                    disciplineID = getInt();
                    if (facade.checkOutDiscipline(disciplineID) || (disciplineID == -1)) break;
                    else System.out.println("Disciplina com esse id nao existe, digite outro.");
                }

                if (disciplineID != -1) {
                    while (true) {
                        System.out.print("Matricula do professor: ");
                        professorID = getInt();
                        if (facade.checkOutProfessor(professorID) || (professorID == -1)) break;
                        else System.out.println("Professor com essa matricula nao existe, digite outra.");
                    }
                    if (professorID != -1) {
                        facade.registerClassroom(id, disciplineID, professorID);
                        System.out.println("Cadastro feito com sucesso!");
                    }
                }
            }
        }
    }

    // tratar ---------------------------------------------------------------

    public static void matriculaAlunos() {
        if (facade.getStudents().size() == 0)
            System.out.println("Nao existe aluno cadastrado para ser matriculado, cadastre um antes.");
        else if (facade.getClassrooms().size() == 0)
            System.out.println("Nao existe turma para adicionar aluno, crie uma antes.");
        else {
            int classroomID;

            while (true) {
                System.out.print("Codigo da turma: ");
                classroomID = getInt();
                if (!facade.checkOutClassroom(classroomID))
                    System.out.println("Turma com esse id nao existe, digite outro.");
                else break;
            }

            boolean stay = true;
            while (stay) {
                int enrollment;
                while (true) {
                    System.out.print("Matricula do aluno (pra sair digite -1): ");
                    enrollment = getInt();

                    if (enrollment < 0) {
                        stay = false;
                        break;
                    } else if (!facade.checkOutStudent(enrollment))
                        System.out.println("Aluno com esse id nÃ£o existe, digite outro.");
                    else if (facade.checkOutStudentInClass(enrollment, classroomID))
                        System.out.println("Aluno jÃ¡ estÃ¡ nessa turma");
                    else break;
                }

                if (stay) facade.registerStudentInClass(enrollment, classroomID);
            }
        }
    }

    public static void exibeTurmasPorAluno() {
        if (facade.getStudents().size() == 0)
            System.out.println("NÃ£o existe aluno cadastrado.");
        else if (facade.getClassrooms().size() == 0)
            System.out.println("NÃ£o existe turma cadastrada.");
        else {
            int enrollment;

            while (true) {
                System.out.print("Matricula do aluno: ");
                enrollment = getInt();

                if (!facade.checkOutStudent(enrollment))
                    System.out.println("Aluno nÃ£o existe, tente outro.");
                else break;
            }

            System.out.println(facade.showAllClassByStudant(enrollment));
        }
    }

    public static void exibeAlunosPorProfessor() {
        if (facade.getStudents().size() == 0)
            System.out.println("NÃ£o existe aluno cadastrado.");
        else if (facade.getProfessors().size() == 0)
            System.out.println("NÃ£o existe professor cadastrado.");
        else {
            int enrollment;

            while (true) {
                System.out.print("Matricula do professor: ");
                enrollment = getInt();

                if (!facade.checkOutProfessor(enrollment))
                    System.out.println("Professor nÃ£o existe, tente outro.");
                else break;
            }

            System.out.println(facade.showAllStudentsByProfessor(enrollment));
        }

    }

    public static void removeTurma() {
        if (facade.getClassrooms().size() == 0)
            System.out.println("NÃ£o existe turma para ser removida.");
        else {
            int classID;

            while (true) {
                System.out.print("Codigo da turma: ");
                classID = getInt();

                if (!facade.checkOutClassroom(classID))
                    System.out.println("Turma nÃ£o pode ser removida pos nÃ£o existe.");
                else break;
            }

            facade.removeClassroom(classID);
        }
    }
}
