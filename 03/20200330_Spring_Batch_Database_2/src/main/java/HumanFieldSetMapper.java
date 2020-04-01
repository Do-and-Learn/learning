import org.springframework.batch.item.file.transform.FieldSet;
import org.springframework.validation.BindException;

public class HumanFieldSetMapper implements org.springframework.batch.item.file.mapping.FieldSetMapper<Human> {
    @Override
    public Human mapFieldSet(FieldSet fieldSet) throws BindException {
        Human human = new Human();
        human.setName(fieldSet.readString("Name"));
        human.setBornYear(fieldSet.readInt("Born Year"));
        human.setBornMonth(fieldSet.readInt("Born Month"));
        human.setHeight(fieldSet.readBigDecimal("Height"));
        return human;
    }
}
