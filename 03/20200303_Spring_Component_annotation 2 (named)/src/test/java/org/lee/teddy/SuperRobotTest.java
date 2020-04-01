package org.lee.teddy;


import org.junit.Assert;
import org.junit.Rule;
import org.junit.Test;
import org.junit.contrib.java.lang.system.SystemOutRule;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(classes = Config.class)
public class SuperRobotTest {

    @Rule  // https://stefanbirkner.github.io/system-rules/index.html
    public final SystemOutRule systemOutRule = new SystemOutRule().enableLog();

    @Autowired
    private Robot teddy;

    @Test
    public void testHi() {
        Assert.assertNotNull(teddy);
        Assert.assertEquals(teddy.getClass(), SuperRobot.class);
        teddy.hi();
        Assert.assertEquals("Hi! I'm a super man ... no I'm a super robot.", systemOutRule.getLog());
    }
}