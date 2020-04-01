import org.springframework.beans.factory.annotation.Autowired;


public class Controller {
    @Autowired
    private HandlerA handlerA;

    @Autowired
    private HandlerB handlerB;

    public HandlerA getHandlerA() {
        return handlerA;
    }

    public HandlerB getHandlerB() {
        return handlerB;
    }
}
