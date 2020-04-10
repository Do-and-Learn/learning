import junit.extensions.TestSetup;
import junit.framework.Test;
import junit.framework.TestSuite;

public class FooTestSetup extends TestSetup {
    public FooTestSetup() {
        super(new TestSuite(FooTest.class));
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

    public static Test suite() {
        return new FooTestSetup();
    }
}
