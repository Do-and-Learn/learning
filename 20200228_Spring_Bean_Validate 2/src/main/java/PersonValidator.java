import org.springframework.validation.Errors;
import org.springframework.validation.Validator;

public class PersonValidator implements Validator {
    @Override
    public boolean supports(Class<?> aClass) {
        return Person.class.isAssignableFrom(aClass);
    }

    @Override
    public void validate(Object o, Errors errors) {
        Person person = (Person) o;
        if (person.getId() == null)
            errors.reject("ID should not be null.");
        else if (person.getId().length() != 10)
            errors.reject("ID length should 10.");
    }
}
