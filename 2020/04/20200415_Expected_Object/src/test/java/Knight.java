import java.util.Objects;

public class Knight extends Role {
    private Weapon weapon = new NoWeapon();

    public Knight() {
        level = 1;
        hp = 100;
    }

    public Knight(int level, int hp) {
        this.level = level;
        this.hp = hp;
    }

    public void attack(Role role) {
        role.hp = role.hp - weapon.hit() - level;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Knight knight = (Knight) o;
        return weapon.equals(knight.weapon);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), weapon);
    }
}
