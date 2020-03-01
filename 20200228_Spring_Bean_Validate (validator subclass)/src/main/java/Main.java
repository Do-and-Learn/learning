import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Main {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(Config.class);
        String hello = context.getBean("hello", String.class);
        System.out.println(hello);  // Should print "Hello world!"
    }
}
