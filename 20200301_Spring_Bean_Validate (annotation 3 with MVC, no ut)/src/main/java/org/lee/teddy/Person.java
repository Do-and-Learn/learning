package org.lee.teddy;

import javax.validation.constraints.NotNull;

public class Person {
    @NotNull
    private String id;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
}
