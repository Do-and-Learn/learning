import org.hibernate.validator.messageinterpolation.ParameterMessageInterpolator;
import org.junit.Assert;
import org.junit.Test;

import javax.validation.ConstraintViolation;
import javax.validation.Validation;
import javax.validation.Validator;
import javax.validation.ValidatorFactory;
import java.util.Set;
import java.util.stream.Collectors;

import static org.hamcrest.Matchers.containsInAnyOrder;

public class ValidatorTest {

    private Validator getValidator() {
        ValidatorFactory factory = Validation.byDefaultProvider().configure().messageInterpolator(new ParameterMessageInterpolator()).buildValidatorFactory();
        return factory.getValidator();
    }

    @Test
    public void testNormalID() {
        Person person = new Person();
        person.setId("A123456789");
        Validator validator = getValidator();
        Set<ConstraintViolation<Person>> constraintViolations = validator.validate(person);

        Assert.assertEquals(0, constraintViolations.size());
    }

    @Test
    public void testInvalidID() {
        Person person = new Person();
        Validator validator = getValidator();
        Set<ConstraintViolation<Person>> constraintViolations = validator.validate(person);

        Assert.assertEquals(1, constraintViolations.size());
        Assert.assertThat(constraintViolations.stream().map(v -> v.getPropertyPath().toString() + ":" + v.getMessage()).collect(Collectors.toList()), containsInAnyOrder("id:ID is invalid."));
    }

}
