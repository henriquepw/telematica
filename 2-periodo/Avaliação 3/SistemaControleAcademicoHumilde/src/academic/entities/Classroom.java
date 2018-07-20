package academic.entities;

import java.util.ArrayList;
import java.util.Date;
import java.util.Objects;

/*
 * Codigo
 * Disciplina
 * Professor
 * Lista de Alunos
 * Horarios de aulas*/
public class Classroom {
    private int id;
    private Discipline discipline;
    private Professor professor;
    private ArrayList<Student> students;
    private ArrayList<Date> hours; // Ver como vai fazer ainda --------------

    public Classroom(int id, Discipline discipline, Professor professor, ArrayList<Student> students, ArrayList<Date> hours) {
        this.id = id;
        this.discipline = discipline;
        this.professor = professor;
        this.students = students;
        this.hours = hours;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Discipline getDiscipline() {
        return discipline;
    }

    public void setDiscipline(Discipline discipline) {
        this.discipline = discipline;
    }

    public Professor getProfessor() {
        return professor;
    }

    public void setProfessor(Professor professor) {
        this.professor = professor;
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
                Objects.equals(discipline, classroom.discipline) &&
                Objects.equals(professor, classroom.professor) &&
                Objects.equals(students, classroom.students) &&
                Objects.equals(hours, classroom.hours);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, discipline, professor, students, hours);
    }

    @Override
    public String toString() {
        return "Classroom{" +
                "id=" + id +
                ", discipline={id=" + discipline.getId() +
                ", name=" + discipline.getName() +
                "}, hours=" + hours +
                ", professor=" + discipline.getName() + '}';
    }
}
