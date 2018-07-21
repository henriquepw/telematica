package academic.controllers;

import academic.entities.Classroom;
import academic.entities.Professor;

import java.util.ArrayList;
import java.util.stream.Collectors;

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

    public boolean addProfessor(Professor professor) {
        var contain = isProfessor(professor.getEnrollment());
        if (!contain) professors.add(professor);

        return !contain;
    }

    public boolean isProfessor(int enrollment) {
        return professors.stream().anyMatch(p -> p.getEnrollment() == enrollment);
    }

    public Professor getProfessor(int enrollment) {
        var professor = professors.stream()
                .filter(p -> p.getEnrollment() == enrollment)
                .collect(Collectors.toList());

        return professor.size() > 0 ? professor.get(0) : null;
    }

    public void addClassroom(int professorID, Classroom classroom) {
        getProfessor(professorID).addClassroom(classroom);
    }

    public void removeClassroom(int classroomID, int professorID) {
        getProfessor(professorID).removeClassroom(classroomID);
    }

}
