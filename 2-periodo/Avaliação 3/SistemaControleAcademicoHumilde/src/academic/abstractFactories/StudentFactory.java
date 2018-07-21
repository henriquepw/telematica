package academic.abstractFactories;

import academic.entities.Discipline;

public interface StudentFactory {
    void addEnrolledDiscipline(Discipline discipline);

    boolean removeEnrolledDIscipline(Discipline discipline);

    boolean completeDiscipline(Discipline discipline);

    boolean inCompletedDIsicpline(Discipline discipline);
}
