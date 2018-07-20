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

    public boolean addProfessor(Professor professor){
        var contain = isProfessor(professor.getEnrollment());
        if (!contain) professors.add(professor);

        return !contain;
    }

    public boolean isProfessor(int enrollment){
        return professors.stream().anyMatch(p -> p.getEnrollment() == enrollment);
    }
}
