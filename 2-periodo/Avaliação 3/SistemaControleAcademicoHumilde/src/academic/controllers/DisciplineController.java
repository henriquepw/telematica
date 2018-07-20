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
        var count = isDiscipline(discipline.getId());
        if (!count) disciplines.add(discipline);

        return count;
    }

    public boolean removeDiscipline(Discipline discipline) {
        return disciplines.remove(discipline);
    }

    public boolean isDiscipline(int id){
        return disciplines.stream().anyMatch(d -> d.getId() == id);
    }
}
