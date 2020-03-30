import org.junit.Assert;
import org.junit.Test;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.datasource.embedded.EmbeddedDatabase;
import org.springframework.jdbc.datasource.embedded.EmbeddedDatabaseBuilder;

import java.util.Arrays;
import java.util.Objects;

import static org.springframework.jdbc.datasource.embedded.EmbeddedDatabaseType.H2;

public class HumanJDBCWriterTest {

    @Test
    public void write() {
        EmbeddedDatabaseBuilder builder = new EmbeddedDatabaseBuilder();
        EmbeddedDatabase dataSource = builder.setType(H2).addScript("file:schema.sql").build();

        JdbcTemplate jdbcTemplate = new JdbcTemplate(dataSource);
        Assert.assertEquals(0L, Objects.requireNonNull(jdbcTemplate.queryForObject("select count(1) from USER", Integer.class)).intValue());
        HumanJDBCWriter writer = new HumanJDBCWriter(dataSource);
        writer.write(Arrays.asList(new Human(), new Human(), new Human()));
        Assert.assertEquals(3L, Objects.requireNonNull(jdbcTemplate.queryForObject("select count(1) from USER", Integer.class)).intValue());
    }
}