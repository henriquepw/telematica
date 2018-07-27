package academic.entities;

import academic.abstractFactories.ClassroomFactory;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

/*
 * Codigo
 * Disciplina
 * Professor
 * Lista de Alunos
 * Horarios de aulas*/
public class Classroom implements ClassroomFactory {
    private int id;
    private int disciplineID;
    private int professorID;
    private ArrayList<Student> students;
    private ArrayList<Date> hours; // Ver como fazer ainda --------------

    public Classroom(int id, int disciplineID, int professorID) {
        this.id = id;
        this.disciplineID = disciplineID;
        this.professorID = professorID;
        this.students = new ArrayList<>();
        this.hours = new ArrayList<>();
    }

    public int getId() {
        return id;
    }

    public int getDisciplineID() {
        return disciplineID;
    }

    public void setDisciplineID(int disciplineID) {
        this.disciplineID = disciplineID;
    }

    public int getProfessorID() {
        return professorID;
    }

    public void setProfessorID(int professorID) {
        this.professorID = professorID;
    }

    public ArrayList<Student> getStudents() {
        return students;
    }

    public void setStudents(ArrayList<Student> students) {
        this.students = students;
    }

    public ArrayList<Date> getHours() {
        return hours;
    }

    public void setHours(ArrayList<Date> hours) {
        this.hours = hours;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Classroom classroom = (Classroom) o;
        return id == classroom.id &&
                disciplineID == classroom.disciplineID &&
                professorID == classroom.professorID &&
                Objects.equals(students, classroom.students) &&
                Objects.equals(hours, classroom.hours);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, disciplineID, professorID, students, hours);
    }

    @Override
    public String toString() {
        return "\nClassroom {" +
                " \n -id= " + id +
                ",\n -disciplineID= " + disciplineID +
                ",\n -professorID= " + professorID +
                ",\n -students= " + students +
                ",\n -hours= " + hours + " }";
    }

    @Override
    public int addStudent(Student student) {
        if (students.stream().noneMatch(s -> s.getEnrollment() == student.getEnrollment()))
            students.add(student);

        return disciplineID;
    }

    @Override
    public boolean removeStudent(int StudentID) {
        Student student = getStudent(StudentID);
        return students.remove(student);
    }

    @Override
    public boolean isStudentClass(int studentID) {
        return students.stream().anyMatch(s -> s.getEnrollment() == studentID);
    }

    @Override
    public Student getStudent(int StudentID) {
        List<Student> student = students.stream().filter(c -> c.getEnrollment() == StudentID).collect(Collectors.toList());
        return (student.size() > 0) ? student.get(0) : null;
    }
}
