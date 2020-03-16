import org.junit.Assert;
import org.junit.Test;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.datasource.embedded.EmbeddedDatabase;
import org.springframework.jdbc.datasource.embedded.EmbeddedDatabaseBuilder;

import static org.springframework.jdbc.datasource.embedded.EmbeddedDatabaseType.H2;


public class SpringBatchTest {
    @Test
    public void testEmbeddedDatabase() {
        EmbeddedDatabaseBuilder builder = new EmbeddedDatabaseBuilder();
        EmbeddedDatabase dataSource = builder.setType(H2).addScript("file:schema.sql").addScript("file:test-data.sql").build();

        JdbcTemplate jdbcTemplate = new JdbcTemplate(dataSource);
        Assert.assertEquals(2, jdbcTemplate.queryForInt("select count(1) from USER"));
        jdbcTemplate.update("INSERT INTO USER (Name, Sex) values ('Bob', 'Boy');");
        jdbcTemplate.update("INSERT INTO USER (Name, Sex) values ('Johnson', 'Unknown');");
        Assert.assertEquals(4, jdbcTemplate.queryForInt("select count(1) from USER"));
    }
}
