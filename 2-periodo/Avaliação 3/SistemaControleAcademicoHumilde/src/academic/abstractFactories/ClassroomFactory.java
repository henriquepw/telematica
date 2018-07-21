package academic.abstractFactories;

import academic.entities.Student;

public interface ClassroomFactory {
    Student getStudent(int StudentID);

    int addStudent(Student student);

    boolean removeStudent(int StudentID);

    boolean isStudentClass(int studentID);
}
