import junit.framework.TestResult;

public class Main {
    public static void main(String[] args) {
        TestResult result= new TestResult();
        FooTestSetup.suite().run(result);
        assert result.runCount() == 1;
        assert result.errorCount() == 0;
    }
}
