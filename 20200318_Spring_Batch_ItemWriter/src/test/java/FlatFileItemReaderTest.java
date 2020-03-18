import org.junit.Assert;
import org.junit.Test;
import org.springframework.batch.item.ExecutionContext;
import org.springframework.batch.item.file.FlatFileItemReader;
import org.springframework.batch.item.file.mapping.DefaultLineMapper;
import org.springframework.batch.item.file.transform.DelimitedLineTokenizer;
import org.springframework.core.io.FileUrlResource;

import java.net.URL;

public class FlatFileItemReaderTest {
    private FlatFileItemReader<Human> reader;

    @Test
    public void testRead() throws Exception {
        reader = new FlatFileItemReader<>();
        reader.setResource(new FileUrlResource(new URL("file:simple.csv")));
        reader.setLinesToSkip(1); // skip header

        DefaultLineMapper<Human> lineMapper = new DefaultLineMapper<>();

        DelimitedLineTokenizer lineTokenizer = new DelimitedLineTokenizer();
        lineTokenizer.setNames("Name", "Born Year", "Born Month", "Height");
        lineMapper.setLineTokenizer(lineTokenizer);
        lineMapper.setFieldSetMapper(new HumanFieldSetMapper());

        reader.setLineMapper(lineMapper);

        reader.open(new ExecutionContext());
        Human human = reader.read();
        int count = 0;
        do {
            Assert.assertNotNull(human);
            count = count + 1;
            System.out.println(human);
            human = reader.read();
        } while (human != null);
        Assert.assertEquals(2, count);
    }
}
