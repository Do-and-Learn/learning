import org.springframework.batch.item.ItemWriter;
import org.springframework.jdbc.core.JdbcTemplate;

import javax.sql.DataSource;
import java.util.List;

public class HumanJDBCWriter implements ItemWriter<Human> {

    private JdbcTemplate jdbcTemplate;

    public HumanJDBCWriter(DataSource ds) {
        this.jdbcTemplate = new JdbcTemplate(ds);
    }

    @Override
    public void write(List<? extends Human> list) {
        for (Human human : list)
            jdbcTemplate.update("INSERT INTO USER (Name, BornYear, BornMonth, Height) values (?, ?, ?, ?);",
                    human.getName(), human.getBornYear(), human.getBornMonth(), human.getHeight());
    }
}
