import org.jmock.Expectations;
import org.junit.Assert;
import org.junit.Test;
import org.springframework.beans.factory.NoSuchBeanDefinitionException;
import org.springframework.beans.factory.UnsatisfiedDependencyException;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class ControllerTest {
    @Test
    public void testGenerateBeans() {
        MockBeansContext<Controller> context = new MockBeansContext<>(new Controller());
        context.start();

        context.getMockery().checking(new Expectations() {{
            //noinspection ResultOfMethodCallIgnored
            allowing(context.getMockObject(HandlerB.class)).getDao();
            will(returnValue(context.getMockObject(Dao.class)));
        }});
        Controller controller = context.getBeanOfObjectUnderTest();

        Assert.assertNotNull(controller.getHandlerA());
        Assert.assertNotNull(controller.getHandlerB());
        Assert.assertNotNull(controller.getHandlerB().getDao());
    }

    @Test
    public void testNotResolveBeans() {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext();
        context.registerBean(Controller.class, Controller::new);

        try {
            context.refresh();
            Assert.fail();
        } catch (UnsatisfiedDependencyException e) {
            Assert.assertEquals(e.getMessage(), "Error creating bean with name 'controller': Unsatisfied dependency expressed through field 'handlerA'; nested exception is org.springframework.beans.factory.NoSuchBeanDefinitionException: No qualifying bean of type 'HandlerA' available: expected at least 1 bean which qualifies as autowire candidate. Dependency annotations: {@org.springframework.beans.factory.annotation.Autowired(required=true)}");
        }

    }
}
