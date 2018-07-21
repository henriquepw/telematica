package academic.controllers;

import academic.entities.Classroom;
import academic.entities.Student;

import java.util.ArrayList;
import java.util.List;
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
        var contain = isClassroom(classroom.getId());
        if (!contain) classrooms.add(classroom);

        return contain;
    }

    public int removeClassroom(int classroomID) {
        var room = getClassroom(classroomID);
        classrooms.remove(room);

        return room.getProfessorID();
    }

    public List<Classroom> showAllClassByStudant(int enrollment) {
        return classrooms.stream()
                .filter(c -> c.isStudentClass(enrollment))
                .collect(Collectors.toList());
    }

    public List<Student> showAllStudentsByProfessor(int professorID) {
        var studant = new ArrayList<Student>();
        var rooms = classrooms.stream()
                .filter(c -> c.getProfessorID() == professorID)
                .collect(Collectors.toList());

        rooms.forEach(r -> r.getStudents().forEach(s -> studant.add(s)));
        return studant;
    }

    public boolean isClassroom(int id) {
        return (classrooms.stream().anyMatch(c -> c.getId() == id));
    }

    public int addStudent(int classroon, Student student) {
        var classroom = classrooms.stream()
                .filter(c -> c.getId() == classroon)
                .collect(Collectors.toList());

        boolean count = true;
        if (classroom.size() > 0)
            count = classroom.get(0).getStudents().stream().anyMatch(s -> s.getEnrollment() == student.getEnrollment());

        if (!count) classroom.get(0).addStudent(student);
        return (!count) ? classroom.get(0).getDisciplineID() : -1;
    }

    public Classroom getClassroom(int id) {
        var rooms = classrooms.stream().filter(c -> c.getId() == id).collect(Collectors.toList());
        return (rooms.size() > 0) ? rooms.get(0) : null;
    }
}
