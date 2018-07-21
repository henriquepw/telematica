package academic.entities;

public class Individual {
    private int enrollment;
    private String name;

    public Individual(int enrollment, String name) {
        this.enrollment = enrollment;
        this.name = name;
    }

    public int getEnrollment() {
        return enrollment;
    }

    public void setEnrollment(int enrollment) {
        this.enrollment = enrollment;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
