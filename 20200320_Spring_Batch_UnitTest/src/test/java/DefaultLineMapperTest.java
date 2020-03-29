import org.junit.Assert;
import org.junit.Test;
import org.springframework.batch.item.file.mapping.DefaultLineMapper;
import org.springframework.batch.item.file.transform.DelimitedLineTokenizer;
import org.springframework.batch.item.file.transform.IncorrectTokenCountException;

import java.math.BigDecimal;

public class DefaultLineMapperTest {
    @Test
    public void testMapLine() throws Exception {
        DefaultLineMapper<Human> lineMapper = new DefaultLineMapper<>();

        DelimitedLineTokenizer lineTokenizer = new DelimitedLineTokenizer();
        lineTokenizer.setNames("Name", "Born Year", "Born Month", "Height");
        lineMapper.setLineTokenizer(lineTokenizer);
        lineMapper.setFieldSetMapper(new HumanFieldSetMapper());

        Human teddy = lineMapper.mapLine("Teddy, 1912, 12, 160.25", 1);

        Assert.assertEquals("Teddy", teddy.getName());
        Assert.assertEquals(1912, teddy.getBornYear());
        Assert.assertEquals(12, teddy.getBornMonth());
        Assert.assertEquals(new BigDecimal("160.25"), teddy.getHeight());
    }

    @Test
    public void testMapLine_wrongDelimiter() throws Exception {
        DefaultLineMapper<Human> lineMapper = new DefaultLineMapper<>();

        DelimitedLineTokenizer lineTokenizer = new DelimitedLineTokenizer();
        lineTokenizer.setNames("Name", "Born Year", "Born Month", "Height");
        lineMapper.setLineTokenizer(lineTokenizer);
        lineMapper.setFieldSetMapper(new HumanFieldSetMapper());

        try {
            lineMapper.mapLine("Teddy\t1912\t12\t160.25", 1);
            Assert.fail();
        } catch (IncorrectTokenCountException e) {
            Assert.assertEquals("Incorrect number of tokens found in record: expected 4 actual 1", e.getMessage());
        }
    }

    @Test
    public void testMapLine_wrongColumns() throws Exception {
        DefaultLineMapper<Human> lineMapper = new DefaultLineMapper<>();

        DelimitedLineTokenizer lineTokenizer = new DelimitedLineTokenizer();
        lineTokenizer.setNames("Name", "Born Year", "Born Month", "Height");
        lineMapper.setLineTokenizer(lineTokenizer);
        lineMapper.setFieldSetMapper(new HumanFieldSetMapper());

        try {
            lineMapper.mapLine("Teddy,1912,12", 1);
            Assert.fail();
        } catch (IncorrectTokenCountException e) {
            Assert.assertEquals("Incorrect number of tokens found in record: expected 4 actual 3", e.getMessage());
        }
    }

    @Test
    public void testMapLine_wrongDataType() throws Exception {
        DefaultLineMapper<Human> lineMapper = new DefaultLineMapper<>();

        DelimitedLineTokenizer lineTokenizer = new DelimitedLineTokenizer();
        lineTokenizer.setNames("Name", "Born Year", "Born Month", "Height");
        lineMapper.setLineTokenizer(lineTokenizer);
        lineMapper.setFieldSetMapper(new HumanFieldSetMapper());

        try {
            lineMapper.mapLine("Teddy,Y1912,12,160.25", 1);
            Assert.fail();
        } catch (NumberFormatException e) {
            Assert.assertEquals("Unparseable number: Y1912", e.getMessage());
        }
    }
}
