import java.math.BigDecimal;

public class Human {

    private String name;
    private int bornYear;
    private int bornMonth;
    private BigDecimal height;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getBornYear() {
        return bornYear;
    }

    public void setBornYear(int bornYear) {
        this.bornYear = bornYear;
    }

    public int getBornMonth() {
        return bornMonth;
    }

    public void setBornMonth(int bornMonth) {
        this.bornMonth = bornMonth;
    }

    public BigDecimal getHeight() {
        return height;
    }

    public void setHeight(BigDecimal height) {
        this.height = height;
    }

    @Override
    public String toString() {
        return "Human{" +
                "name='" + name + '\'' +
                ", bornYear=" + bornYear +
                ", bornMonth=" + bornMonth +
                ", height=" + height +
                '}';
    }
}
