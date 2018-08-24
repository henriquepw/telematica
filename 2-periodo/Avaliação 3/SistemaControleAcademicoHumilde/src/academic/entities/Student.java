package academic.entities;

import academic.abstractFactories.StudentFactory;

import java.util.ArrayList;
import java.util.Objects;

/*
 * Matricula
 * Nome
 * curso
 * CRE(Coeficiente de rendimento escolar)
 * curso
 * lista de disciplinas cursadas
 * lista de disciplinas cursand
 */
public class Student extends Individual implements StudentFactory {
    private float cre;
    private String course;
    private ArrayList<Discipline> completedDisciplines;
    private ArrayList<Discipline> enrolledDisciplines;
    private final short MAX_DISCIPLINES = 6;

    public Student(int enrollment, String name, String course) {
        super(enrollment, name);
        this.course = course;
        this.cre = 0;
        this.completedDisciplines = new ArrayList<>();
        this.enrolledDisciplines = new ArrayList<>();
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

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Student student = (Student) o;
        return getEnrollment() == student.getEnrollment() &&
                Float.compare(student.cre, cre) == 0 &&
                Objects.equals(getName(), student.getName()) &&
                Objects.equals(course, student.course) &&
                Objects.equals(completedDisciplines, student.completedDisciplines) &&
                Objects.equals(enrolledDisciplines, student.enrolledDisciplines);
    }

    @Override
    public int hashCode() {
        return Objects.hash(getEnrollment(), getName(), cre, course, completedDisciplines, enrolledDisciplines);
    }

    @Override
    public String toString() {
        return "\nname {" + name +
                " \n -enrollment= " + getEnrollment() +
                ",\n -cre= " + cre +
                ",\n -course= " + course +
                ",\n -completedDisciplines= " + completedDisciplines +
                ",\n -enrolledDisciplines= " + enrolledDisciplines + '}';
    }

    @Override
    public boolean inCompletedDIsicpline(Discipline discipline) {
        return completedDisciplines.stream().anyMatch(d -> d.equals(discipline));
    }

    @Override
    public boolean completeDiscipline(Discipline discipline) {
        boolean count = this.enrolledDisciplines.remove(discipline);
        if (count) this.completedDisciplines.add(discipline);

        return count;
    }

    @Override
    public void addEnrolledDiscipline(Discipline discipline) {
        if (enrolledDisciplines.size() == MAX_DISCIPLINES)
            System.out.println("Limite de discilpinas que podem ser pagas ao mesmo tempo atingido!");

        else if (inCompletedDIsicpline(discipline))
            System.out.println("Aluno já pagou essa disciplina!");

        else if (enrolledDisciplines.stream().anyMatch(e -> e.getId() == discipline.getId()))
            System.out.println("Aluno já paga essa disciplina!");

        else this.enrolledDisciplines.add(discipline);
    }

    @Override
    public boolean removeEnrolledDIscipline(Discipline discipline) {
        return this.enrolledDisciplines.remove(discipline);
    }


}
