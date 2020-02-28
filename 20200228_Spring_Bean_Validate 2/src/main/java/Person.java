import javax.validation.constraints.Min;
import javax.validation.constraints.NotBlank;

public class Person {
    @NotBlank
    private String name;

    @Min(value = 18, message = "Age should not be less than {value}")
    private int age;

    private String id;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
}
