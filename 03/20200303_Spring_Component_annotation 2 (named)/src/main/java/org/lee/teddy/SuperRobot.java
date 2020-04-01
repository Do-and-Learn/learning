package org.lee.teddy;

import org.springframework.stereotype.Component;

@Component("teddy")
public class SuperRobot extends Robot {
    @Override
    public void hi() {
        System.out.print("Hi! I'm a super man ... no I'm a super robot.");
    }
}
