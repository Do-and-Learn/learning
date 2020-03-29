import org.jmock.Mockery;
import org.jmock.lib.concurrent.Synchroniser;
import org.jmock.lib.legacy.ClassImposteriser;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.GenericApplicationContext;

import java.lang.reflect.Field;
import java.util.*;

@SuppressWarnings({"rawtypes", "unchecked"})
public class MockBeansContext<T> {

    private final Mockery mockery;
    private final GenericApplicationContext context;
    private final Class<T> classUnderTest;
    private Map<RequiredBean, Object> mockObjects = new HashMap<>();

    public MockBeansContext(T objectUnderTest) {
        classUnderTest = (Class<T>) objectUnderTest.getClass();
        context = new AnnotationConfigApplicationContext();
        mockery = new Mockery() {{
            setImposteriser(ClassImposteriser.INSTANCE);
            setThreadingPolicy(new Synchroniser());
        }};
        Set<RequiredBean> autowiredFields = collectAllRequiredBeans(objectUnderTest.getClass());
        for (RequiredBean requiredBean : autowiredFields) {
            Object mockObject = mockery.mock(requiredBean.type, requiredBean.name);
            context.registerBean(requiredBean.name, requiredBean.type, () -> mockObject);
            mockObjects.put(requiredBean, mockObject);
        }
        context.registerBean(classUnderTest, () -> objectUnderTest);
    }

    private Set<RequiredBean> collectAllRequiredBeans(Class<?> cls) {
        Set<RequiredBean> result = new HashSet<>();
        for (Field field : cls.getDeclaredFields()) {
            if (Arrays.stream(field.getDeclaredAnnotations()).anyMatch(annotation -> annotation.annotationType() == Autowired.class)) {
                String name;
                if (Arrays.stream(field.getDeclaredAnnotations()).anyMatch(annotation -> annotation.annotationType() == Qualifier.class)) {
                    name = field.getAnnotation(Qualifier.class).value();
                } else {
                    name = field.getName();
                }
                result.add(new RequiredBean(field.getType(), name));
                result.addAll(collectAllRequiredBeans(field.getType()));
            }
        }
        return result;
    }

    public T getBeanOfObjectUnderTest() {
        try {
            return context.getBean(classUnderTest);
        } catch (IllegalStateException e) {
            if (e.getMessage().endsWith("has not been refreshed yet"))
                throw new IllegalStateException("Before getting the bean, you should call start() first.", e);
            throw e;
        }
    }

    public <T1> T1 getMockObject(Class<T1> cls) {
        for (RequiredBean bean : mockObjects.keySet()) {
            if (bean.type == cls) {
                return (T1) mockObjects.get(bean);
            }
        }
        throw new RuntimeException("Cannot get bean which class is [" + cls + "]");
    }

    public void start() {
        try {
            context.refresh();
        } catch (IllegalStateException e) {
            if (e.getMessage().endsWith("does not support multiple refresh attempts: just call 'refresh' once"))
                throw new IllegalStateException("start() does not support to call multiple times.", e);
            throw e;
        }
    }

    public Mockery getMockery() {
        return mockery;
    }

    public GenericApplicationContext getContext() {
        return context;
    }

    private static class RequiredBean {
        public final String name;
        public final Class type;

        public RequiredBean(Class type, String name) {
            this.name = name;
            this.type = type;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            RequiredBean that = (RequiredBean) o;
            return Objects.equals(name, that.name) &&
                    Objects.equals(type, that.type);
        }

        @Override
        public int hashCode() {
            return Objects.hash(name, type);
        }
    }
}
