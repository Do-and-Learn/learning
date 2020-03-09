package org.lee.teddy;


import org.junit.Assert;
import org.junit.Rule;
import org.junit.Test;
import org.junit.contrib.java.lang.system.SystemOutRule;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@ContextConfiguration("classpath:beans.xml")
@RunWith(SpringJUnit4ClassRunner.class)
public class JavaConfigTest {
    @Rule
    public final SystemOutRule systemOutRule = new SystemOutRule().enableLog();

    @Autowired
    private Human human;

    @Autowired
    private Human teddy;

    @Autowired
    private Robot teddyControl;

    @Autowired
    private Robot robot;

    @Test
    public void testHuman() {
        Assert.assertEquals("Nobody", human.getName());
        robot.hi();
        Assert.assertEquals("Hi! I'm Nobody.", systemOutRule.getLog());
    }

    @Test
    public void testTeddy() {
        Assert.assertEquals("Teddy", teddy.getName());
        teddyControl.hi();
        Assert.assertEquals("Hi! I'm Teddy.", systemOutRule.getLog());
    }
}
