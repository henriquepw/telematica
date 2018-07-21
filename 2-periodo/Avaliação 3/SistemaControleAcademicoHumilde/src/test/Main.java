package test;

import academic.controllers.ClassroomController;
import academic.controllers.DisciplineController;
import academic.controllers.ProfessorController;
import academic.controllers.StudentController;
import academic.entities.Classroom;
import academic.entities.Discipline;
import academic.entities.Professor;
import academic.entities.Student;

import java.util.*;
import java.util.stream.Collectors;

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

        disciplineController.addDiscipline(new Discipline(1, 10, "programação 2", "Estridutara de dados e poo"));
        professorController.addProfessor(new Professor(2020, "Marcelo"));
        studentController.addStudent(new Student(2017, "Henrique", "Telemática"));
        classroomController.addClassroom(new Classroom(101, 1, 2020));
        classroomController.addStudent(101, new Student(2017, "Henrique", "Telemática"));
        professorController.addClassroom(2020, new Classroom(101, 1, 2020));
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
                    System.out.println(disciplineController.getDisciplines().toString());
                    break;
                case 22: // Exibir todas os professores
                    System.out.println(professorController.getProfessors().toString());
                    break;
                case 33: // Exibir todas as turmas
                    System.out.println(classroomController.getClassrooms().toString());
                    break;
                case 44: // Exibir todas os alunos
                    System.out.println(studentController.getStudents().toString());
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

        var count = disciplineController.addDiscipline(new Discipline(id, hours, name, description));
        if (!count) System.out.println("Disciplina com esse id já existe");
    }

    public static void cadastroProfessor() {
        var s = new Scanner(System.in);

        System.out.print("Nome: ");
        var name = s.nextLine();
        System.out.print("Matricula: ");
        var enrollment = s.nextInt();

        var count = professorController.addProfessor(new Professor(enrollment, name));
        if (!count) System.out.println("Professor com essa matricula já existe");
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

        var count = studentController.addStudent(new Student(enrollment, name, course));
        if (!count) System.out.println("Aluno com esse id já existe");
    }

    public static void cadastroTurma() {
        var s = new Scanner(System.in);
        int id, disciplineID, professorID;

        if (disciplineController.getDisciplines().size() == 0)
            System.out.println("Cadastre uma disciplina antes de cadastrar uma turma.");
        else if (professorController.getProfessors().size() == 0)
            System.out.println("Cadastre um professor antes de cadastrar uma turma.");
        else {
            while (true) {
                System.out.print("Codigo da turma: ");
                id = s.nextInt();
                if (classroomController.isClassroom(id))
                    System.out.println("Turma com esse id já existe, digite outra.");
                else break;
            }

            while (true) {
                System.out.print("Codigo da disciplina: ");
                disciplineID = s.nextInt();
                if (!disciplineController.isDiscipline(disciplineID))
                    System.out.println("Disciplina com esse id não existe, digite outro.");
                else break;
            }

            while (true) {
                System.out.print("Matricula do professor: ");
                professorID = s.nextInt();
                if (!professorController.isProfessor(professorID))
                    System.out.println("Professor com essa matricula não existe, digite outra.");
                else break;
            }

            var classroom = new Classroom(id, disciplineID, professorID);
            professorController.addClassroom(professorID, classroom);
            classroomController.addClassroom(classroom);
        }
    }

    public static void matriculaAlunos() {
        if (studentController.getStudents().size() == 0)
            System.out.println("Não existe aluno cadastrado para ser matriculado, cadastre um antes.");
        else if (classroomController.getClassrooms().size() == 0)
            System.out.println("Não existe turma para adicionar aluno, crie uma antes.");
        else {
            var s = new Scanner(System.in);
            int classroomID;
            Student studant;

            while (true) {
                System.out.print("Codigo da turma: ");
                classroomID = s.nextInt();
                if (!classroomController.isClassroom(classroomID))
                    System.out.println("Turma com esse id não existe, digite outro.");
                else break;
            }

            boolean stay = true;
            while (stay) {
                int studantID;
                while (true) {
                    System.out.print("Matricula do aluno (pra sair digite -1): ");
                    studantID = s.nextInt();

                    if (studantID < 0) {
                        stay = false;
                        break;
                    } else if (!studentController.isStudent(studantID))
                        System.out.println("Aluno com esse id não existe, digite outro.");
                    else if (classroomController.getClassroom(classroomID).isStudentClass(studantID))
                        System.out.println("Aluno já está nessa turma");
                    else break;
                }

                final int finalStudantID = studantID;
                if (stay) {
                    studant = studentController.getStudents().stream()
                            .filter(st -> st.getEnrollment() == finalStudantID)
                            .collect(Collectors.toList()).get(0);

                    final int finalDisciplineID = classroomController.addStudent(classroomID, studant);

                    var discipline = disciplineController.getDisciplines().stream()
                            .filter(d -> d.getId() == finalDisciplineID)
                            .collect(Collectors.toList()).get(0);

                    studant.addEnrolledDiscipline(discipline);
                }
            }
        }
    }

    public static void exibeTurmasPorAluno() {
        if (studentController.getStudents().size() == 0)
            System.out.println("Não existe aluno cadastrado.");
        else if (classroomController.getClassrooms().size() == 0)
            System.out.println("Não existe turma cadastrada.");
        else {
            var s = new Scanner(System.in);
            int enrollment;

            while (true) {
                System.out.print("Matricula do aluno: ");
                enrollment = s.nextInt();

                if (!studentController.isStudent(enrollment))
                    System.out.println("Aluno não existe, tente outro.");
                else break;
            }

            System.out.println(classroomController.showAllClassByStudant(enrollment));
        }
    }

    public static void exibeAlunosPorProfessor() {
        if (studentController.getStudents().size() == 0)
            System.out.println("Não existe aluno cadastrado.");
        else if (professorController.getProfessors().size() == 0)
            System.out.println("Não existe professor cadastrado.");
        else {
            var s = new Scanner(System.in);
            int enrollment;

            while (true) {
                System.out.print("Matricula do professor: ");
                enrollment = s.nextInt();

                if (!professorController.isProfessor(enrollment))
                    System.out.println("Professor não existe, tente outro.");
                else break;
            }

            System.out.println(classroomController.showAllStudentsByProfessor(enrollment));
        }

    }

    public static void removeTurma() {
        if (classroomController.getClassrooms().size() == 0)
            System.out.println("Não existe turma para ser removida.");
        else {
            var s = new Scanner(System.in);
            int classID;

            while (true) {
                System.out.print("Codigo da turma: ");
                classID = s.nextInt();

                if (!classroomController.isClassroom(classID))
                    System.out.println("Turma não pode ser removida pos não existe.");
                else break;
            }

            professorController.removeClassroom(
                    classroomController.getClassroom(classID).getId(),
                    classroomController.removeClassroom(classID));

        }
    }
}
