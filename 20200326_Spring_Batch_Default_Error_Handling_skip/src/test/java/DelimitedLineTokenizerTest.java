import org.junit.Assert;
import org.junit.Test;
import org.springframework.batch.item.file.transform.DelimitedLineTokenizer;
import org.springframework.batch.item.file.transform.FieldSet;
import org.springframework.batch.item.file.transform.IncorrectTokenCountException;

import java.math.BigDecimal;

public class DelimitedLineTokenizerTest {
    private DelimitedLineTokenizer lineTokenizer;

    @Test
    public void testTokenize() {
        lineTokenizer = new DelimitedLineTokenizer();
        lineTokenizer.setNames("Name", "Born Year", "Born Month", "Height");
        FieldSet fieldSet = lineTokenizer.tokenize("Teddy, 1912, 12, 160.25");
        Assert.assertEquals("Teddy", fieldSet.readString("Name"));
        Assert.assertEquals(1912, fieldSet.readInt("Born Year"));
        Assert.assertEquals(12, fieldSet.readInt("Born Month"));
        Assert.assertEquals(new BigDecimal("160.25"), fieldSet.readBigDecimal("Height"));
    }

    @Test
    public void testTokenize_delimiter() {
        lineTokenizer = new DelimitedLineTokenizer();
        lineTokenizer.setNames("Name", "Born Year", "Born Month", "Height");
        lineTokenizer.setDelimiter("\t");
        FieldSet fieldSet = lineTokenizer.tokenize("Teddy\t1912\t12\t160.25");
        Assert.assertEquals("Teddy", fieldSet.readString("Name"));
        Assert.assertEquals(1912, fieldSet.readInt("Born Year"));
        Assert.assertEquals(12, fieldSet.readInt("Born Month"));
        Assert.assertEquals(new BigDecimal("160.25"), fieldSet.readBigDecimal("Height"));
    }

    @Test(expected = IncorrectTokenCountException.class)
    public void testTokenize_missing_column() {
        lineTokenizer = new DelimitedLineTokenizer();
        lineTokenizer.setNames("Name", "Born Year", "Born Month", "Height");
        lineTokenizer.tokenize("Teddy, 1912, 12");
    }

    @Test(expected = IncorrectTokenCountException.class)
    public void testTokenize_wrong_delimiter() {
        lineTokenizer = new DelimitedLineTokenizer();
        lineTokenizer.setNames("Name", "Born Year", "Born Month", "Height");
        lineTokenizer.setDelimiter("\t");
        lineTokenizer.tokenize("Teddy, 1912, 12");
    }

    @Test(expected = IncorrectTokenCountException.class)
    public void testTokenize_wrong_delimiter2() {
        lineTokenizer = new DelimitedLineTokenizer();
        lineTokenizer.setNames("Name", "Born Year", "Born Month", "Height");
        lineTokenizer.tokenize("Teddy\t1912\t12");
    }
}
