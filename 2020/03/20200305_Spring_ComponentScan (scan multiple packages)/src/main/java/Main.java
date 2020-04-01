import org.lee.teddy.Config;
import org.lee.teddy.Robot;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Main {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(Config.class);
        Robot robot = context.getBean(Robot.class);
        robot.hi();
    }
}
