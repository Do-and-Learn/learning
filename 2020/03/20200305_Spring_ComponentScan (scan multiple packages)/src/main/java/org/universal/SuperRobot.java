package org.universal;

import org.springframework.stereotype.Component;

@Component("teddy")
public class SuperRobot {
    public void hi() {
        System.out.print("Hi! I'm a super man ... no I'm a super robot.");
    }
}
