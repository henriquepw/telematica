package academic.entities;

public class Individual {
    protected int enrollment;
    protected String name;

    public Individual(int enrollment, String name) {
        this.enrollment = enrollment;
        this.name = name;
    }

    public int getEnrollment() {
        return enrollment;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
