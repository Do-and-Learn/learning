import org.junit.Before;
import org.junit.Test;
import org.testng.Assert;

public class KnightTest {

    private Knight attacker;
    private Knight attackee;

    @Before
    public void setUp() {
        attacker = new Knight();
        attackee = new Knight();
    }

    @Test
    public void testAttack() {
        int initHp = attackee.getHp();
        attacker.attack(attackee);
        // Procedural State Verification
        Knight actual = new Knight(1, initHp - 1);
        Assert.assertEquals(attackee, actual);
    }
}