package org.lee.teddy.model;

import com.fasterxml.jackson.annotation.JsonCreator;

import java.util.Arrays;
import java.util.stream.Collectors;

public enum Sex {
    Boy, Girl, None;

    @JsonCreator
    public static Sex forValue(String value) {
        StringBuilder sb = new StringBuilder(value.toLowerCase());
        sb.setCharAt(0, Character.toUpperCase(value.charAt(0)));
        try {
            return Sex.valueOf(sb.toString());
        } catch (IllegalArgumentException e) {
            throw new IllegalArgumentException("Cannot deserialize value from String [" + value + "]: value not noe of [" + Arrays.stream(Sex.values()).map(Sex::toString).collect(Collectors.joining(", ")) + "]");
        }
    }
}
