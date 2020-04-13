public class Knight {
    private int level = 1;
    private Weapon weapon = new NoWeapon();

    public int hit() {
        return level + weapon.hit();
    }

    public void levelUp() {
        level = level + 1;
    }

    public void equip(Weapon weapon) {
        this.weapon = weapon;
    }
}
