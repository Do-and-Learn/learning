import org.junit.Assert;
import org.junit.Test;

import java.util.Map;
import java.util.TreeMap;

public class Main {
    @Test
    public void testCaseInsensitiveMap() {
        Map<String, String> map = new TreeMap<String, String>(String.CASE_INSENSITIVE_ORDER);
        map.put("FOO", "F00");

        Assert.assertEquals("F00", map.get("foo"));
        Assert.assertEquals("F00", map.get("Foo"));
        Assert.assertEquals("F00", map.get("FOO"));
        Assert.assertNull(map.get("F00"));
        Assert.assertTrue(map.containsKey("Foo"));
        Assert.assertFalse(map.containsKey("F00"));
    }
}
