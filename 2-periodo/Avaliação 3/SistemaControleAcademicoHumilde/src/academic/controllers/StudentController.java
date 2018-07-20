package academic.controllers;

import academic.entities.Student;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class StudentController {
    private ArrayList<Student> students;

    public StudentController() {
        students = new ArrayList<>();
    }

    public ArrayList<Student> getStudents() {
        return students;
    }

    public void setStudents(ArrayList<Student> students) {
        this.students = students;
    }

    public boolean addStudent(Student student) {
        var contain = isStudent(student.getEnrollment());
        if (!contain) students.add(student);

        return !contain;
    }

    public boolean removeStudent(Student student) {
        var contain = students.remove(student);
        return contain;
    }

    public List<Student> getStudent(int enrollment) {
        return students.stream()
                .filter(s -> s.getEnrollment() == enrollment)
                .collect(Collectors.toList());
    }

    public boolean isStudent(int enrollment) {
        return students.stream().anyMatch(s -> s.getEnrollment() == enrollment);
    }

}
