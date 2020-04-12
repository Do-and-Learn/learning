import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestResult;

public class FooTestCase extends TestCase {
    private Test decoratedSuite;

    public FooTestCase(Test test) {
        decoratedSuite = test;
    }

    @Override
    protected void setUp() throws Exception {
        super.setUp();
        System.out.println("setUp");
    }

    @Override
    protected void tearDown() throws Exception {
        super.tearDown();
        System.out.println("tearDown");
    }

    @Override
    public TestResult run() {
        TestResult result = new TestResult();
        try {
            setUp();
            decoratedSuite.run(result);
            tearDown();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        return result;
    }
}
