package academic.entities;

import java.util.ArrayList;

/*
 * Matricula
 * NOme
 * Classes lecionadas
 * maximo de turma que pode ser lecionadas por 1 professor
 */
public class Professor {
    private int enrollment;
    private String name;
    private ArrayList<Classroom> classrooms;
    private final short MAX_CLASSROOMS = 6;

    public Professor(int enrollment, String name) {
        this.enrollment = enrollment;
        this.name = name;
        this.classrooms = new ArrayList<>();
    }

    public int getEnrollment() {
        return enrollment;
    }

    public void setEnrollment(int enrollment) {
        this.enrollment = enrollment;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ArrayList<Classroom> getClassrooms() {
        return classrooms;
    }

    public void setClassrooms(ArrayList<Classroom> classrooms) {
        this.classrooms = classrooms;
    }


}



















