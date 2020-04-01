package org.lee.teddy;


import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.universal.SuperRobot;

@ContextConfiguration(classes = {TypeSafeScan2Test.class})
@ComponentScan(basePackageClasses = {Robot.class, SuperRobot.class})
@RunWith(SpringJUnit4ClassRunner.class)
public class TypeSafeScan2Test {
    @Autowired(required = false)
    private Robot extreme;

    @Autowired(required = false)
    private SuperRobot teddy;

    @Test
    public void testRobot() {
        Assert.assertNotNull(extreme);
    }

    @Test
    public void testSuperRobot() {
        Assert.assertNotNull(teddy);
    }
}
