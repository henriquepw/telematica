package academic.entities;

import java.util.ArrayList;

/*
 * Matricula
 * Nome
 * curso
 * CRE(Coeficiente de rendimento escolar)
 * curso
 * lista de disciplinas cursadas
 * lista de disciplinas cursand
 */
public class Student {
    private int enrollment;
    private String name;
    private float cre;
    private String course;
    private ArrayList<Discipline> completedDisciplines;
    private ArrayList<Discipline> enrolledDisciplines;
    private final short MAX_DISCIPLINES = 6;

    public Student(int enrollment, String name, String course) {
        this.enrollment = enrollment;
        this.name = name;
        this.course = course;
        this.cre = 0;
        this.completedDisciplines = new ArrayList<>();
        this.enrolledDisciplines = new ArrayList<>();
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

    public float getCre() {
        return cre;
    }

    public void setCre(float cre) {
        this.cre = cre;
    }

    public String getCourse() {
        return course;
    }

    public void setCourse(String course) {
        this.course = course;
    }

    public ArrayList<Discipline> getCompletedDisciplines() {
        return completedDisciplines;
    }

    public void setCompletedDisciplines(ArrayList<Discipline> completedDisciplines) {
        this.completedDisciplines = completedDisciplines;
    }

    public ArrayList<Discipline> getEnrolledDisciplines() {
        return enrolledDisciplines;
    }

    public void setEnrolledDisciplines(ArrayList<Discipline> enrolledDisciplines) {
        this.enrolledDisciplines = enrolledDisciplines;
    }

    private boolean inCompletedDIsicpline(Discipline discipline) {
        var count = completedDisciplines.stream().anyMatch(d -> d.equals(discipline));
        return count;
    }

    public boolean registerEnrolledDiscipline(Discipline discipline) {
        var count = false;

        if (this.enrolledDisciplines.size() == MAX_DISCIPLINES)
            System.out.println("Limite de discilpinas que podem ser pagas ao mesmo tempo atingido!");
        else if (inCompletedDIsicpline(discipline))
            System.out.println("Aluno já pagou essa disciplina!");
        else
            this.enrolledDisciplines.add(discipline);

        return count;
    }

    public boolean completeDiscipline(Discipline discipline) {
        var count = this.enrolledDisciplines.remove(discipline);

        if (count)
            this.completedDisciplines.add(discipline);

        return count;
    }

    public boolean removeEnrolledDIscipline(Discipline discipline) {
        return this.enrolledDisciplines.remove(discipline);
    }
}
