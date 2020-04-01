package org.lee.teddy;


import org.junit.Assert;
import org.junit.Rule;
import org.junit.Test;
import org.junit.contrib.java.lang.system.SystemOutRule;
import org.junit.runner.RunWith;
import org.lee.SuperRobot;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(classes = Config.class)
public class SuperRobotTest {

    @Rule  // https://stefanbirkner.github.io/system-rules/index.html
    public final SystemOutRule systemOutRule = new SystemOutRule().enableLog();

    @Autowired(required = false)
    private SuperRobot teddy;

    @Test
    public void testHi() {
        Assert.assertNull(teddy);
    }
}