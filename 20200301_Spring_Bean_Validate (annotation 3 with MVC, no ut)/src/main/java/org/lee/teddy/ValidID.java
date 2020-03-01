package org.lee.teddy;

import javax.validation.Constraint;
import javax.validation.Payload;
import javax.validation.ReportAsSingleViolation;
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@ReportAsSingleViolation
@Target(ElementType.FIELD)
@Retention(RetentionPolicy.RUNTIME)
@Constraint(validatedBy = {IDValidator.class})
public @interface ValidID {
    String message() default "ID is invalid.";

    Class<?>[] groups() default {};

    Class<? extends Payload>[] payload() default {};
}
