import org.springframework.beans.factory.annotation.Autowired;

public class HandlerB {
    @Autowired
    private Dao dao;

    public Dao getDao() {
        return dao;
    }
}
