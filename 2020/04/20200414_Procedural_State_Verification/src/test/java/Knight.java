public class Knight extends Role {
    private Weapon weapon = new NoWeapon();

    public Knight() {
        level = 1;
        hp = 100;
    }

    public void attack(Role role) {
        role.hp = role.hp - weapon.hit() - level;
    }
}
