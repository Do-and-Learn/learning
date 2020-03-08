package org.lee.teddy;


import org.junit.Assert;
import org.junit.Rule;
import org.junit.Test;
import org.junit.contrib.java.lang.system.SystemOutRule;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@ContextConfiguration(classes = {JavaConfigTest.class})
@Configuration
@RunWith(SpringJUnit4ClassRunner.class)
public class JavaConfigTest {
    @Rule
    public final SystemOutRule systemOutRule = new SystemOutRule().enableLog();

    @Autowired
    private Robot teddyControl;

    @Autowired
    private Robot bobControl;

    @Autowired
    private Robot robot;

    @Test
    public void testRobot() {
        robot.hi();
        Assert.assertEquals("Hi! I'm Nobody.", systemOutRule.getLog());
    }

    @Test
    public void testTeddy() {
        teddyControl.hi();
        Assert.assertEquals("Hi! I'm Teddy.", systemOutRule.getLog());
    }

    @Test
    public void testBob() {
        bobControl.hi();
        Assert.assertEquals("Hi! I'm Bob.", systemOutRule.getLog());
    }

    @Bean
    public Robot robot() {
        return new HumanControl(new Human("Nobody"));
    }

    @Bean
    public Robot bobControl(Human bob) {
        return new HumanControl(bob);
    }

    @Bean
    public Robot teddyControl(Human teddy) {
        return new HumanControl(teddy);
    }

    @Bean
    public Human teddy() {
        return new Human("Teddy");
    }

    @Bean
    public Human bob() {
        return new Human("Bob");
    }
}
