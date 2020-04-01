package org.lee.teddy;


import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.universal.SuperRobot;

@ContextConfiguration(classes = {JavaConfigTest.class})
@Configuration
@RunWith(SpringJUnit4ClassRunner.class)
public class JavaConfigTest {
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
        Assert.assertNull(teddy);
    }

    @Bean
    public Robot extreme() {
        return new ExtremeRobot();
    }
}
