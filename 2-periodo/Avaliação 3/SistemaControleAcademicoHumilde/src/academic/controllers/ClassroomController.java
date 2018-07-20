package academic.controllers;

import academic.entities.Classroom;
import academic.entities.Student;

import java.util.ArrayList;
import java.util.stream.Collectors;

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
        var count = isClassroom(classroom.getId());
        if (!count) classrooms.add(classroom);

        return count;
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

        return classrooms;
    }

    public boolean isClassroom(int id) {
        return (classrooms.stream().anyMatch(c -> c.getId() == id));
    }

    public boolean addStudent(int turma, Student student) {
        var classroom = classrooms.stream()
                .filter(c -> c.getId() == turma)
                .collect(Collectors.toList());

        boolean count = true;
        if (classroom.size() > 0)
            count = classroom.get(0).getStudents().stream().anyMatch(s -> s.getEnrollment() == student.getEnrollment());

        if (!count) classroom.get(0).addStudent(student);
        return count;
    }
}
