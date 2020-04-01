package org.lee.teddy;


import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@ContextConfiguration(classes = {JavaConfigTest.DevConfig.class, JavaConfigTest.ProdConfig.class})
@RunWith(SpringJUnit4ClassRunner.class)
@ActiveProfiles("dev")
public class JavaConfigTest {

    @Autowired(required = false)
    private Human human;

    @Test
    public void testDev() {
        Assert.assertNotNull(human);
        Assert.assertEquals("developer", human.getName());
    }

    @Profile("dev")
    @Configuration
    public static class DevConfig {
        @Bean
        public Human developer() {
            Human human = new Human();
            human.setName("developer");
            return human;
        }
    }

    @Profile("prod")
    @Configuration
    public static class ProdConfig {
        @Bean
        public Human customer() {
            Human human = new Human();
            human.setName("customer");
            return human;
        }
    }
}