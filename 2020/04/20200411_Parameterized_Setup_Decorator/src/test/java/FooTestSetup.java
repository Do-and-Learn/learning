import junit.extensions.TestSetup;
import junit.framework.Test;

public class FooTestSetup extends TestSetup {
    public FooTestSetup(Test test) {
        super(test);
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
}
