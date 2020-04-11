import junit.framework.TestResult;
import junit.framework.TestSuite;

public class Main {
    public static void main(String[] args) {
        TestResult result= new TestResult();
        new FooTestSetup(new TestSuite(FooTest.class)).run(result);
        assert result.runCount() == 1;
        assert result.errorCount() == 0;
    }
}
