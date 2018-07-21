package academic.entities;

import academic.abstractFactories.ProfessorFactory;

import java.util.ArrayList;
import java.util.Objects;
import java.util.stream.Collectors;

/*
 * Matricula
 * NOme
 * Classes lecionadas
 * maximo de turma que pode ser lecionadas por 1 professor
 */
public class Professor extends Individual implements ProfessorFactory {
    private int enrollment;
    private String name;
    private ArrayList<Classroom> classrooms;
    private final short MAX_CLASSROOMS = 6;

    public Professor(int enrollment, String name) {
        super(enrollment, name);
        this.classrooms = new ArrayList<>();
    }

    public ArrayList<Classroom> getClassrooms() {
        return classrooms;
    }

    public void setClassrooms(ArrayList<Classroom> classrooms) {
        this.classrooms = classrooms;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Professor professor = (Professor) o;
        return enrollment == professor.enrollment &&
                Objects.equals(name, professor.name) &&
                Objects.equals(classrooms, professor.classrooms);
    }

    @Override
    public int hashCode() {
        return Objects.hash(enrollment, name, classrooms);
    }

    @Override
    public String toString() {
        return "\nProfessor {" +
                "  \n -Enrollment= " + enrollment +
                ", \n -Name= " + name +
                ", \n -Classrooms= " + classrooms + " }";
    }

    @Override
    public void addClassroom(Classroom classroom) {
        if (this.classrooms.size() == MAX_CLASSROOMS)
            System.out.println("Limite de turmas lecionadas atingido!");

        else if (classrooms.stream().anyMatch(c -> c.getId() == classroom.getId()))
            System.out.println("Professor já leciona essa turma!");

        else this.classrooms.add(classroom);
    }

    @Override
    public void removeClassroom(int classroomID) {
        classrooms.remove(getClassroom(classroomID));
    }

    @Override
    public Classroom getClassroom(int ClassroomID) {
        var rooms = classrooms.stream().filter(c -> c.getId() == ClassroomID).collect(Collectors.toList());
        return (rooms.size() > 0) ? rooms.get(0) : null;
    }
}



















