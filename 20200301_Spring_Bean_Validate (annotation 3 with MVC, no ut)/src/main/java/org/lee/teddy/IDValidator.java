package org.lee.teddy;

import javax.validation.ConstraintValidator;
import javax.validation.ConstraintValidatorContext;

public class IDValidator implements ConstraintValidator<ValidID, String> {

    @Override
    public boolean isValid(String id, ConstraintValidatorContext constraintValidatorContext) {
        if (id == null)
            return false;
        else return id.length() == 10;
    }
}
