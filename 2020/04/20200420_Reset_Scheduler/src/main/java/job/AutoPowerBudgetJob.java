package job;

import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;
import org.springframework.scheduling.quartz.QuartzJobBean;

import java.text.SimpleDateFormat;
import java.util.Date;

public class AutoPowerBudgetJob extends QuartzJobBean {

    public static final String DEFAULT_JOB_CRON_EXPRESSION = "* * * ? * *";  // every second

    @Override
    protected void executeInternal(JobExecutionContext jobContext) throws JobExecutionException {
        String pattern = "HH:mm:ss";
        SimpleDateFormat simpleDateFormat = new SimpleDateFormat(pattern);
        String date = simpleDateFormat.format(new Date());
        System.out.println("[" + date + "] executeInternal");
        try {
            Thread.sleep(10000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        date = simpleDateFormat.format(new Date());
        System.out.println("[" + date + "] end");
    }
}
