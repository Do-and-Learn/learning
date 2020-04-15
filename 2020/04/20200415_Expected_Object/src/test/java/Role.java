import java.util.Objects;

public class Role {
    protected int level;
    protected int hp;

    public int getHp() {
        return hp;
    }

    public int getLevel() {
        return level;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Role role = (Role) o;
        return level == role.level &&
                hp == role.hp;
    }

    @Override
    public int hashCode() {
        return Objects.hash(level, hp);
    }
}
