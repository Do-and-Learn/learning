import org.apache.commons.io.IOUtils;
import org.junit.Assert;
import org.junit.Test;

import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

public class ZipInputStreamTest {
    @Test
    public void testDecompress() throws Exception {
        FileInputStream fis = new FileInputStream("simple.zip");
        ZipInputStream zis = new ZipInputStream(new BufferedInputStream(fis));
        ZipEntry entry = zis.getNextEntry();
        Assert.assertEquals("README.md", entry.getName());
        entry = zis.getNextEntry();
        Assert.assertEquals("simple.csv", entry.getName());
    }
}
