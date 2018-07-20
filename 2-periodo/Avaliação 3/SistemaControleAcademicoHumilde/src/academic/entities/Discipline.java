package academic.entities;

import java.util.ArrayList;
import java.util.Date;
import java.util.Objects;


/*
 * Identificador
 * Nome
 * Descrição
 * Carga horaria
 */
public class Discipline {
    private int id;
    private int hours;
    private String name;
    private String description;

    public Discipline(int id, int hours, String name, String description) {
        this.id = id;
        this.hours = hours;
        this.name = name;
        this.description = description;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getHours() {
        return hours;
    }

    public void setHours(int hours) {
        this.hours = hours;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Discipline that = (Discipline) o;
        return id == that.id &&
                hours == that.hours &&
                Objects.equals(name, that.name) &&
                Objects.equals(description, that.description);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, hours, name, description);
    }

    @Override
    public String toString() {
        return "\nDiscipline {" + id + ": " +
                "\n -Hours: " + hours +
                "\n -Name: " + name +
                "\n -Description: " + description + " }";
    }
}