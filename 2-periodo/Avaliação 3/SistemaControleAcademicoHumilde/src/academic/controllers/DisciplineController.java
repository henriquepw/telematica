package academic.controllers;

import academic.entities.Discipline;

import java.util.ArrayList;

public class DisciplineController {
    private ArrayList<Discipline> disciplines;

    public DisciplineController() {
        this.disciplines = new ArrayList<>();
    }

    public ArrayList<Discipline> getDisciplines() {
        return disciplines;
    }

    public void setDisciplines(ArrayList<Discipline> disciplines) {
        this.disciplines = disciplines;
    }

    public boolean addDiscipline(Discipline discipline) {
        var count = disciplines.stream().anyMatch(d -> d.getId() == discipline.getId());

        if (!count) disciplines.add(discipline);

        return count;

        //return (!count)? disciplines.add(discipline): false;
    }

    public boolean removeDiscipline(Discipline discipline) {
        return disciplines.remove(discipline);
    }

}
