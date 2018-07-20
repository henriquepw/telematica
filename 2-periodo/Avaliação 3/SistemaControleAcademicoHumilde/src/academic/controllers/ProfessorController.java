package academic.controllers;

import academic.entities.Professor;

import java.util.ArrayList;

public class ProfessorController {
    ArrayList<Professor> professors;

    public ProfessorController() {
        this.professors = new ArrayList<>();
    }

    public ArrayList<Professor> getProfessors() {
        return professors;
    }

    public void setProfessors(ArrayList<Professor> professors) {
        this.professors = professors;
    }

    public boolean registerProfessor(Professor professor){
        var contain = false;
        for (Professor p : professors)
            if (p.getEnrollment() == professor.getEnrollment()) {
                contain = true;
                break;
            }

        if (!contain) professors.add(professor);

        return !contain;
    }
}
