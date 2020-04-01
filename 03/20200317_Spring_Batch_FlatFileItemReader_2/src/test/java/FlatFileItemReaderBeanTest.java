import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.batch.item.ExecutionContext;
import org.springframework.batch.item.file.FlatFileItemReader;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@ContextConfiguration("classpath:beans.xml")
@RunWith(SpringJUnit4ClassRunner.class)
public class FlatFileItemReaderBeanTest {
    @Autowired
    private FlatFileItemReader<Human> reader;

    @Test
    public void testReader() throws Exception {
        Assert.assertNotNull(reader);
        reader.open(new ExecutionContext());
        Human human = reader.read();
        int count = 0;
        do {
            Assert.assertNotNull(human);
            count = count + 1;
            human = reader.read();
        } while (human != null);
        Assert.assertEquals(2, count);
    }
}
