package academic.facede;

import academic.controllers.ClassroomController;
import academic.controllers.DisciplineController;
import academic.controllers.ProfessorController;
import academic.controllers.StudentController;
import academic.entities.Classroom;
import academic.entities.Discipline;
import academic.entities.Professor;
import academic.entities.Student;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Facede {
    private ClassroomController classroomController;
    private DisciplineController disciplineController;
    private ProfessorController professorController;
    private StudentController studentController;

    public Facede() {
        this.classroomController = new ClassroomController();
        this.disciplineController = new DisciplineController();
        this.professorController = new ProfessorController();
        this.studentController = new StudentController();
    }

    public ArrayList<Discipline> getDisciplines() {
        return disciplineController.getDisciplines();
    }

    public ArrayList<Professor> getProfessors() {
        return professorController.getProfessors();
    }

    public ArrayList<Student> getStudents() {
        return studentController.getStudents();
    }

    public ArrayList<Classroom> getClassrooms() {
        return classroomController.getClassrooms();
    }

    public boolean checkOutDiscipline(int disciplineID) {
        return disciplineController.isDiscipline(disciplineID);
    }

    public boolean checkOutProfessor(int professorID) {
        return professorController.isProfessor(professorID);
    }

    public boolean checkOutStudent(int studentID) {
        return studentController.isStudent(studentID);
    }

    public boolean checkOutClassroom(int classroomID) {
        return classroomController.isClassroom(classroomID);
    }

    public boolean checkOutStudentInClass(int enrollment, int classroomID) {
        return classroomController.getClassroom(classroomID).isStudentClass(enrollment);
    }

    public boolean registerDiscipline(int DisciplineID, int hours, String name, String description) {
        return disciplineController.addDiscipline(new Discipline(DisciplineID, hours, name, description));
    }

    public boolean registerProfessor(int enrollment, String name) {
        return professorController.addProfessor(new Professor(enrollment, name));
    }

    public boolean registerStudent(int enrollment, String name, String course) {
        return studentController.addStudent(new Student(enrollment, name, course));
    }

    public void registerClassrooom(int classroomID, int disciplineID, int professorID) {
        var classroom = new Classroom(classroomID, disciplineID, professorID);

        professorController.addClassroom(professorID, classroom);
        classroomController.addClassroom(classroom);
    }

    public void registerStudentInClass(int enrollment, int classroomID) {
        var studant = getStudents().stream()
                .filter(st -> st.getEnrollment() == enrollment)
                .collect(Collectors.toList()).get(0);

        final int finalDisciplineID = classroomController.addStudent(classroomID, studant);
        var discipline = getDisciplines().stream()
                .filter(d -> d.getId() == finalDisciplineID)
                .collect(Collectors.toList()).get(0);

        studant.addEnrolledDiscipline(discipline);
    }

    public List<Classroom> showAllClassByStudant(int enrollment) {
        return classroomController.showAllClassByStudant(enrollment);
    }

    public List<Student> showAllStudentsByProfessor(int enrollment) {
        return classroomController.showAllStudentsByProfessor(enrollment);
    }

    public void removeClassroom(int classroomID) {
        professorController.removeClassroom(
                classroomController.getClassroom(classroomID).getId(),
                classroomController.removeClassroom(classroomID));
    }
}
