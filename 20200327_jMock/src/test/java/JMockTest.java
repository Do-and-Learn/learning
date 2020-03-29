import org.jmock.Expectations;
import org.jmock.Mockery;
import org.jmock.imposters.ByteBuddyClassImposteriser;
import org.junit.Test;

public class JMockTest {
    private Mockery context = new Mockery() {{
        setImposteriser(ByteBuddyClassImposteriser.INSTANCE);
    }};

    @Test
    public void testOneSubscriberReceivesAMessage() {
        // set up
        final Subscriber subscriber = context.mock(Subscriber.class);

        Publisher publisher = new Publisher();
        publisher.add(subscriber);

        final String message = "message";

        // expectations
        context.checking(new Expectations() {{
            oneOf(subscriber).receive(message);
        }});

        // execute
        publisher.publish(message);

        // verify
        context.assertIsSatisfied();
    }
}
