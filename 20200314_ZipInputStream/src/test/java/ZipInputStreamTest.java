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
        Assert.assertNotNull(entry);
        Assert.assertEquals("simple.csv", entry.getName());
        byte[] full = IOUtils.readFully(zis, (int) entry.getSize());
        Assert.assertEquals(String.join("\r\n",
                "Name, Born Year, Born Month, Height",
                "Teddy, 1912, 12, 160.25",
                "Bob, 1911, 10, 180.11"), new String(full));
    }
}
