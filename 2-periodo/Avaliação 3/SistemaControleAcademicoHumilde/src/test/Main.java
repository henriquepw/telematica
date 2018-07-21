package test;

import academic.entities.Student;
import academic.facede.Facede;

import java.util.*;

public class Main {
    public static Facede facede;

    public static void main(String[] args) {
        facede = new Facede();

        facede.registerDiscipline(1, 10, "programação 2", "Estridutara de dados e poo");
        facede.registerProfessor(2020, "Marcelo");
        facede.registerStudent(2017, "Henrique", "Telemática");
        facede.registerClassrooom(101, 1, 2020);
        facede.registerStudentInClass(2017, 101);
        menu();
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

        return new Scanner(System.in).nextInt();
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
                    System.out.println(facede.getDisciplines().toString());
                    break;
                case 22: // Exibir todas os professores
                    System.out.println(facede.getProfessors().toString());
                    break;
                case 33: // Exibir todas as turmas
                    System.out.println(facede.getClassrooms().toString());
                    break;
                case 44: // Exibir todas os alunos
                    System.out.println(facede.getStudents().toString());
                    break;
                case 0:
                    stay = false;
                    break;
                default:
                    System.out.println("Comando invalido");
            }
    }

    public static void cadastroDisciplina() {
        var s = new Scanner(System.in);

        System.out.print("Id: ");
        var id = s.nextInt();
        System.out.print("Carga horaria: ");
        var hours = s.nextInt();
        System.out.print("Nome: ");
        s.nextLine();
        var name = s.nextLine();
        System.out.print("Descrição: ");
        var description = s.nextLine();

        if (!facede.registerDiscipline(id, hours, name, description))
            System.out.println("Erro: Disciplina com esse id já existe");
    }

    public static void cadastroProfessor() {
        var s = new Scanner(System.in);

        System.out.print("Nome: ");
        var name = s.nextLine();
        System.out.print("Matricula: ");
        var enrollment = s.nextInt();

        if (!facede.registerProfessor(enrollment, name))
            System.out.println("Erro: Professor com essa matricula já existe");
    }

    public static void cadastroAluno() {
        var s = new Scanner(System.in);

        System.out.print("Nome: ");
        var name = s.nextLine();
        System.out.print("Matricula: ");
        var enrollment = s.nextInt();
        s.nextLine();
        System.out.print("Curso: ");
        String course = s.nextLine();

        if (!facede.registerStudent(enrollment, name, course))
            System.out.println("Aluno com esse id já existe");
    }

    public static void cadastroTurma() {
        var s = new Scanner(System.in);
        int id, disciplineID, professorID;

        if (facede.getDisciplines().size() == 0)
            System.out.println("Cadastre uma disciplina antes de cadastrar uma turma.");
        else if (facede.getProfessors().size() == 0)
            System.out.println("Cadastre um professor antes de cadastrar uma turma.");
        else {
            while (true) {
                System.out.print("Codigo da turma: ");
                id = s.nextInt();
                if (facede.checkOutClassroom(id))
                    System.out.println("Turma com esse id já existe, digite outra.");
                else break;
            }

            while (true) {
                System.out.print("Codigo da disciplina: ");
                disciplineID = s.nextInt();
                if (!facede.checkOutDiscipline(disciplineID))
                    System.out.println("Disciplina com esse id não existe, digite outro.");
                else break;
            }

            while (true) {
                System.out.print("Matricula do professor: ");
                professorID = s.nextInt();
                if (!facede.checkOutProfessor(professorID))
                    System.out.println("Professor com essa matricula não existe, digite outra.");
                else break;
            }

            facede.registerClassrooom(id, disciplineID, professorID);
        }
    }

    public static void matriculaAlunos() {
        if (facede.getStudents().size() == 0)
            System.out.println("Não existe aluno cadastrado para ser matriculado, cadastre um antes.");
        else if (facede.getClassrooms().size() == 0)
            System.out.println("Não existe turma para adicionar aluno, crie uma antes.");
        else {
            var s = new Scanner(System.in);
            int classroomID;
            Student studant;

            while (true) {
                System.out.print("Codigo da turma: ");
                classroomID = s.nextInt();
                if (!facede.checkOutClassroom(classroomID))
                    System.out.println("Turma com esse id não existe, digite outro.");
                else break;
            }

            boolean stay = true;
            while (stay) {
                int enrollment;
                while (true) {
                    System.out.print("Matricula do aluno (pra sair digite -1): ");
                    enrollment = s.nextInt();

                    if (enrollment < 0) {
                        stay = false;
                        break;
                    } else if (!facede.checkOutStudent(enrollment))
                        System.out.println("Aluno com esse id não existe, digite outro.");
                    else if (facede.checkOutStudentInClass(enrollment, classroomID))
                        System.out.println("Aluno já está nessa turma");
                    else break;
                }

                if (stay) facede.registerStudentInClass(enrollment, classroomID);
            }
        }
    }

    public static void exibeTurmasPorAluno() {
        if (facede.getStudents().size() == 0)
            System.out.println("Não existe aluno cadastrado.");
        else if (facede.getClassrooms().size() == 0)
            System.out.println("Não existe turma cadastrada.");
        else {
            var s = new Scanner(System.in);
            int enrollment;

            while (true) {
                System.out.print("Matricula do aluno: ");
                enrollment = s.nextInt();

                if (!facede.checkOutStudent(enrollment))
                    System.out.println("Aluno não existe, tente outro.");
                else break;
            }

            System.out.println(facede.showAllClassByStudant(enrollment));
        }
    }

    public static void exibeAlunosPorProfessor() {
        if (facede.getStudents().size() == 0)
            System.out.println("Não existe aluno cadastrado.");
        else if (facede.getProfessors().size() == 0)
            System.out.println("Não existe professor cadastrado.");
        else {
            var s = new Scanner(System.in);
            int enrollment;

            while (true) {
                System.out.print("Matricula do professor: ");
                enrollment = s.nextInt();

                if (!facede.checkOutProfessor(enrollment))
                    System.out.println("Professor não existe, tente outro.");
                else break;
            }

            System.out.println(facede.showAllStudentsByProfessor(enrollment));
        }

    }

    public static void removeTurma() {
        if (facede.getClassrooms().size() == 0)
            System.out.println("Não existe turma para ser removida.");
        else {
            var s = new Scanner(System.in);
            int classID;

            while (true) {
                System.out.print("Codigo da turma: ");
                classID = s.nextInt();

                if (!facede.checkOutClassroom(classID))
                    System.out.println("Turma não pode ser removida pos não existe.");
                else break;
            }

            facede.removeClassroom(classID);
        }
    }
}
