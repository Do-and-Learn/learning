import org.junit.Test;
import org.testng.Assert;

public class KnightTest {

    private static Knight knight = new Knight();

    @Test
    public void testInit() {
        Assert.assertEquals(knight.hit(), 1);
    }

    @Test
    public void testLevel2Hit() {
        knight.levelUp();
        Assert.assertEquals(knight.hit(), 2);
    }

    @Test
    public void testLevel3Hit() {
        knight.levelUp();
        Assert.assertEquals(knight.hit(), 3);
    }

    @Test
    public void testLevel4Hit() {
        knight.levelUp();
        Assert.assertEquals(knight.hit(), 4);
    }

    @Test
    public void testWithKnife() {
        Knife knife = new Knife();
        knight.equip(knife);
        Assert.assertEquals(knight.hit(), 4 + knife.hit());
    }
}