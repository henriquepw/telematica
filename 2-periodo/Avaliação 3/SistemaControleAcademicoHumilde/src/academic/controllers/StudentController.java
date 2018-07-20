package academic.controllers;

import academic.entities.Discipline;
import academic.entities.Student;

import java.util.ArrayList;

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
         /* var contain = students.stream()
                .anyMatch(s -> s.getEnrollment() == student.getEnrollment());
        */
        /* var contain = students.parallelStream()
                .anyMatch(s -> s.getEnrollment() == student.getEnrollment());
         */

        var contain = false;
        for (Student s : students)
            if (s.getEnrollment() == student.getEnrollment()) {
                contain = true;
                break;
            }

        if (!contain) students.add(student);

        return !contain;
    }

    public boolean removeStudent(Student student) {
        var contain = students.remove(student);
        return contain;
    }


}
