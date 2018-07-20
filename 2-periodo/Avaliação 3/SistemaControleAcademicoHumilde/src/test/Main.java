package test;

import academic.controllers.ClassroomController;
import academic.controllers.DisciplineController;
import academic.controllers.ProfessorController;
import academic.controllers.StudentController;
import academic.entities.Discipline;
import academic.entities.Professor;
import academic.entities.Student;

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
        Scanner s = new Scanner(System.in);
        boolean stay = true;
        while (stay) {
            String name;
            int enrollment;
            boolean count;

            switch (options()) {
                case 1:
                    System.out.print("Id: ");
                    var id = s.nextInt();
                    System.out.print("Carga horaria: ");
                    var hours = s.nextInt();
                    System.out.print("Nome: ");
                    s.nextLine();
                    name = s.nextLine();
                    System.out.print("Descrição: ");
                    var description = s.nextLine();

                    count = disciplineController.addDiscipline(new Discipline(id, hours, name, description));
                    if (!count) System.out.println("Disciplina com esse id já existe");
                    break;
                case 2:
                    System.out.print("Nome: ");
                    name = s.nextLine();
                    System.out.print("Matricula: ");
                    enrollment = s.nextInt();

                    count = professorController.addProfessor(new Professor(enrollment, name));
                    if (!count) System.out.println("Professor com esse id já existe");
                    break;
                case 3:

                    break;
                case 4:

                    break;
                case 5:

                    break;
                case 6:
                    System.out.print("Matricula do aluno: ");
                    classroomController.showAllClassByStudant(s.nextInt());
                    break;
                case 7:
                    System.out.print("Matricula do professor: ");
                    //classroomController.showAllStudantByProfessor(s.nextInt());
                    break;
                case 8:
                    System.out.print("Nome: ");
                    name = s.nextLine();
                    System.out.print("Matricula: ");
                    enrollment = s.nextInt();
                    System.out.print("Curso: ");
                    String course = s.nextLine();

                    count = studentController.addStudent(new Student(enrollment, name, course));
                    if (!count) System.out.println("Aluno com esse id já existe");
                    break;
                case 11:
                    System.out.println(disciplineController.getDisciplines().toString());
                    break;
                case 22:
                    System.out.println(professorController.getProfessors().toString());
                    break;
                case 33:
                    System.out.println(classroomController.getClassrooms().toString());
                    break;
                case 0:
                    stay = false;
                    break;
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

        System.out.println("Extras: ");
        System.out.println("8. Cadastar aluno");

        System.out.println("11. Exibir disciplinas");
        System.out.println("22. Exibir professores");
        System.out.println("33. Exibir turmas");
        System.out.println("0. Sair");

        return new Scanner(System.in).nextInt();
    }
}
