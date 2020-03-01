import javax.validation.Constraint;
import javax.validation.Payload;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

//@ReportAsSingleViolation
//@Target(ElementType.FIELD)
@Retention(RetentionPolicy.RUNTIME)
@Constraint(validatedBy = {IDValidator.class})
public @interface ValidID {
    String message() default "ID is invalid.";

    Class<?>[] groups() default {};

    Class<? extends Payload>[] payload() default {};
}
