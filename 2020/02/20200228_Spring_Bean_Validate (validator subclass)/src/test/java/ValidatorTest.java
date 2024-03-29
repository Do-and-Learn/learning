import org.hibernate.validator.messageinterpolation.ParameterMessageInterpolator;
import org.junit.Assert;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.ExpectedException;
import org.springframework.context.support.DefaultMessageSourceResolvable;
import org.springframework.validation.DirectFieldBindingResult;
import org.springframework.validation.Errors;
import org.springframework.validation.ValidationUtils;

import javax.validation.ConstraintViolation;
import javax.validation.Validation;
import javax.validation.Validator;
import javax.validation.ValidatorFactory;
import java.util.Set;
import java.util.stream.Collectors;

import static org.hamcrest.Matchers.containsInAnyOrder;

public class ValidatorTest {
    @Test
    public void testNormalNameAndAge() {
        Person person = new Person();
        person.setName("Teddy");
        person.setAge(18);
        Validator validator = getValidator();
        Set<ConstraintViolation<Person>> constraintViolations = validator.validate(person);

        Assert.assertEquals(0, constraintViolations.size());
    }

    private Validator getValidator() {
        ValidatorFactory factory = Validation.byDefaultProvider().configure().messageInterpolator(new ParameterMessageInterpolator()).buildValidatorFactory();
        return factory.getValidator();
    }

    @Test
    public void testInvalidNameAndAge() {
        Person person = new Person();
        Validator validator = getValidator();
        Set<ConstraintViolation<Person>> constraintViolations = validator.validate(person);

        Assert.assertEquals(2, constraintViolations.size());
        Assert.assertThat(constraintViolations.stream().map(v -> v.getPropertyPath().toString() + ":" + v.getMessage()).collect(Collectors.toList()), containsInAnyOrder("name:must not be blank", "age:Age should not be less than 18"));
    }

    @Test
    public void testInvalidName_nullName() {
        Person person = new Person();
        person.setAge(18);
        Validator validator = getValidator();
        Set<ConstraintViolation<Person>> constraintViolations = validator.validate(person);

        Assert.assertEquals(1, constraintViolations.size());
        Assert.assertThat(constraintViolations.stream().map(v -> v.getPropertyPath().toString() + ":" + v.getMessage()).collect(Collectors.toList()), containsInAnyOrder("name:must not be blank"));
    }

    @Test
    public void testInvalidName_emptyName() {
        Person person = new Person();
        person.setAge(18);
        person.setName("");
        Validator validator = getValidator();
        Set<ConstraintViolation<Person>> constraintViolations = validator.validate(person);

        Assert.assertEquals(1, constraintViolations.size());
        Assert.assertThat(constraintViolations.stream().map(v -> v.getPropertyPath().toString() + ":" + v.getMessage()).collect(Collectors.toList()), containsInAnyOrder("name:must not be blank"));
    }

    @Test
    public void testInvalidNaAge_noAge() {
        Person person = new Person();
        person.setName("Hello");
        Validator validator = getValidator();
        Set<ConstraintViolation<Person>> constraintViolations = validator.validate(person);

        Assert.assertEquals(1, constraintViolations.size());
        Assert.assertThat(constraintViolations.stream().map(v -> v.getPropertyPath().toString() + ":" + v.getMessage()).collect(Collectors.toList()), containsInAnyOrder("age:Age should not be less than 18"));
    }

    @Test
    public void testInvalidNaAge_smallAge() {
        Person person = new Person();
        person.setName("Hello");
        person.setAge(17);
        Validator validator = getValidator();
        Set<ConstraintViolation<Person>> constraintViolations = validator.validate(person);

        Assert.assertEquals(1, constraintViolations.size());
        Assert.assertThat(constraintViolations.stream().map(v -> v.getPropertyPath().toString() + ":" + v.getMessage()).collect(Collectors.toList()), containsInAnyOrder("age:Age should not be less than 18"));
    }

    @Test
    public void testPersonValidator() {
        PersonValidator validator = new PersonValidator();
        Assert.assertTrue(validator.supports(Person.class));
        Assert.assertFalse(validator.supports(String.class));

        Person person = new Person();
        Errors errors = new DirectFieldBindingResult(person, "person");

        Assert.assertFalse(errors.hasErrors());
        ValidationUtils.invokeValidator(validator, person, errors);
        Assert.assertTrue(errors.hasErrors());
        Assert.assertEquals(1, errors.getErrorCount());
        Assert.assertThat(errors.getAllErrors().stream().map(DefaultMessageSourceResolvable::getCode).collect(Collectors.toList()), containsInAnyOrder("ID should not be null."));
    }

    @Rule
    public ExpectedException exceptionRule = ExpectedException.none();

    @Test
    public void testPersonValidatorWithWrongObject() {
        exceptionRule.expect(IllegalArgumentException.class);
        exceptionRule.expectMessage("Validator [class PersonValidator] does not support [class java.lang.Object]");

        PersonValidator validator = new PersonValidator();
        Errors errors = new DirectFieldBindingResult(null, "person");
        ValidationUtils.invokeValidator(validator, new Object(), errors);
    }
}
