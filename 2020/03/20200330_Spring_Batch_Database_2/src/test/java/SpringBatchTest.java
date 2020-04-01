import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.batch.core.*;
import org.springframework.batch.core.launch.JobLauncher;
import org.springframework.batch.core.repository.JobExecutionAlreadyRunningException;
import org.springframework.batch.core.repository.JobInstanceAlreadyCompleteException;
import org.springframework.batch.core.repository.JobRestartException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.jdbc.Sql;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import java.util.Objects;


@ContextConfiguration(locations = {"classpath:beans.xml", "classpath:config.xml"})
@RunWith(SpringJUnit4ClassRunner.class)
@Sql({"file:schema.sql"})
public class SpringBatchTest {

    @Autowired
    private JobLauncher jobLauncher;

    @Autowired
    private Job job;

    @Autowired
    private JdbcTemplate jdbcTemplate;

    @Before
    public void setup() {
        jdbcTemplate.update("delete from USER");
    }

    @Test
    public void testSimple() throws JobParametersInvalidException, JobExecutionAlreadyRunningException, JobRestartException, JobInstanceAlreadyCompleteException {
        JobExecution execution;
        Assert.assertEquals(0, Objects.requireNonNull(jdbcTemplate.queryForObject("select count(1) from USER", Integer.class)).intValue());
        execution = jobLauncher.run(job, new JobParametersBuilder().addString("inputFile", "simple.csv").addLong("timestamp", System.currentTimeMillis()).toJobParameters());
        Assert.assertEquals(2, Objects.requireNonNull(jdbcTemplate.queryForObject("select count(1) from USER", Integer.class)).intValue());
        Assert.assertEquals(ExitStatus.COMPLETED, execution.getExitStatus());
        execution = jobLauncher.run(job, new JobParametersBuilder().addString("inputFile", "simple.csv").addLong("timestamp", System.currentTimeMillis()).toJobParameters());
        Assert.assertEquals(4, Objects.requireNonNull(jdbcTemplate.queryForObject("select count(1) from USER", Integer.class)).intValue());
        Assert.assertEquals(ExitStatus.COMPLETED, execution.getExitStatus());
    }

    @Test
    public void testSimpleError() throws JobParametersInvalidException, JobExecutionAlreadyRunningException, JobRestartException, JobInstanceAlreadyCompleteException {
        Assert.assertEquals(0, Objects.requireNonNull(jdbcTemplate.queryForObject("select count(1) from USER", Integer.class)).intValue());
        JobExecution execution = jobLauncher.run(job, new JobParametersBuilder().addString("inputFile", "simple_error1.csv").addLong("timestamp", System.currentTimeMillis()).toJobParameters());
        Assert.assertEquals(4, Objects.requireNonNull(jdbcTemplate.queryForObject("select count(1) from USER", Integer.class)).intValue()); // Actually the job read three records, and commit-interval="2".
        Assert.assertEquals(ExitStatus.COMPLETED, execution.getExitStatus());
        Assert.assertEquals(0, execution.getAllFailureExceptions().size());
        StepExecution step = execution.getStepExecutions().stream().findFirst().orElse(null);
        Assert.assertNotNull(step);
        Assert.assertEquals(4, step.getReadCount());
        Assert.assertEquals(4, step.getWriteCount());
    }

    @Test
    public void testSimpleError2() throws JobParametersInvalidException, JobExecutionAlreadyRunningException, JobRestartException, JobInstanceAlreadyCompleteException {
        Assert.assertEquals(0, Objects.requireNonNull(jdbcTemplate.queryForObject("select count(1) from USER", Integer.class)).intValue());
        JobExecution execution = jobLauncher.run(job, new JobParametersBuilder().addString("inputFile", "simple_error2.csv").addLong("timestamp", System.currentTimeMillis()).toJobParameters());
        Assert.assertEquals(2, Objects.requireNonNull(jdbcTemplate.queryForObject("select count(1) from USER", Integer.class)).intValue()); // Actually the job read three records, and commit-interval="2".
        Assert.assertEquals(ExitStatus.FAILED, execution.getExitStatus());
        Assert.assertEquals(1, execution.getAllFailureExceptions().size());
        Assert.assertEquals("Skip limit of '1' exceeded", execution.getAllFailureExceptions().get(0).getMessage());
        StepExecution step = execution.getStepExecutions().stream().findFirst().orElse(null);
        Assert.assertNotNull(step);
        Assert.assertEquals(3, step.getReadCount());
        Assert.assertEquals(2, step.getWriteCount());
    }
}
