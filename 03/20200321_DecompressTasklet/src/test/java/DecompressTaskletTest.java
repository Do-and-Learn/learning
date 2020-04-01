import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import java.io.File;

@ContextConfiguration(locations = {"classpath:beans.xml", "classpath:config.xml"})
@RunWith(SpringJUnit4ClassRunner.class)
public class DecompressTaskletTest {
    @Autowired
    private DecompressTasklet decompressTasklet;

    @Test
    public void testDecompressTasklet() throws Exception {
        Assert.assertNotNull(decompressTasklet);
        File target = new File(decompressTasklet.getTargetFile());
        if (target.exists())
            Assert.assertTrue(target.delete());
        Assert.assertFalse(target.exists());
        decompressTasklet.execute(null, null);
        Assert.assertTrue(target.exists());
    }
}
