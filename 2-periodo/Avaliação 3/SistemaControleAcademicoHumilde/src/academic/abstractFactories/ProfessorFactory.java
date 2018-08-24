package academic.abstractFactories;

import academic.entities.Classroom;

public interface ProfessorFactory {
    Classroom getClassroom(int ClassroomID);

    void addClassroom(Classroom classroom);

    void removeClassroom(int classroomID);
}
