package org.lee.teddy;

import javax.inject.Named;

/*
<dependency>
  <groupId>javax.inject</groupId>
  <artifactId>javax.inject</artifactId>
  <version>1</version>
</dependency>
* */

@Named("extreme")
public class ExtremeRobot extends Robot {
    @Override
    public void hi() {
        System.out.print("Hi! I'm the best.");
    }
}
