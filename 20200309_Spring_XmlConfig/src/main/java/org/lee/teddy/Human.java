package org.lee.teddy;

public class Human {
    private String name;

    public Human() {
        this("Nobody");
    }

    public Human(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}
