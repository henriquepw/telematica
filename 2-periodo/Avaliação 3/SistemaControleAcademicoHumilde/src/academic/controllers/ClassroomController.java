package academic.controllers;

import academic.entities.Classroom;

import java.util.ArrayList;

public class ClassroomController {
    private ArrayList<Classroom> classrooms;

    public ClassroomController() {
        this.classrooms = new ArrayList<>();
    }

    public ArrayList<Classroom> getClassrooms() {
        return classrooms;
    }

    public void setClassrooms(ArrayList<Classroom> classrooms) {
        this.classrooms = classrooms;
    }

    public boolean addClassroom(Classroom classroom) {
        var count = classrooms.stream().anyMatch(d -> d.getId() == classroom.getId());

        if (!count) classrooms.add(classroom);

        return count;

        //return (!count)? disciplines.add(discipline): false;
    }

    public boolean removeDiscipline(Classroom classroom) {
        return classrooms.remove(classroom);
    }

    public ArrayList<String> showAllClassByStudant(int enrollment) {
        var classrooms = new ArrayList<String>();

        this.classrooms.forEach(c ->
                c.getStudents().forEach(s -> {
                    if (s.getEnrollment() == enrollment)
                        classrooms.add(c.toString());
                })
        );

        /*
        this.classrooms.forEach(c -> c.getStudents().stream()
                .filter(s -> s.getEnrollment() == enrollment)
                .map(s -> c.toString()).forEach(classrooms::add)
        );
        */

        /*
        this.classrooms.forEach(c -> c.getStudents().stream()
                .filter(s -> s.getEnrollment() == enrollment)
                .map(s -> classrooms.add(c.toString()))
        );
         */

        return classrooms;
    }
}
