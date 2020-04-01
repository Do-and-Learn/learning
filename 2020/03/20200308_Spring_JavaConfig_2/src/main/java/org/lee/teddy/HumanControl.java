package org.lee.teddy;

public class HumanControl implements Robot {
    private Human controller;

    public Human getController() {
        return controller;
    }

    public HumanControl(Human controller) {
        this.controller = controller;
    }

    @Override
    public void hi() {
        System.out.print(String.format("Hi! I'm %s.", controller.getName()));
    }
}
