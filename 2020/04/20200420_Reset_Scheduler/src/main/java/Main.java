import org.quartz.TriggerKey;
import org.quartz.impl.StdScheduler;
import org.quartz.impl.triggers.CronTriggerImpl;
import org.springframework.context.support.GenericXmlApplicationContext;

public class Main {

    public static void main(String[] args) {
        final GenericXmlApplicationContext context = new GenericXmlApplicationContext("job.xml");
        final StdScheduler scheduler = (StdScheduler) context.getBean("scheduler");

        new Thread() {
            @Override
            public void run() {
                try {
                    Thread.sleep(1000);
                    scheduler.pauseAll();
                    CronTriggerImpl trigger = context.getBean("trigger", CronTriggerImpl.class);
                    trigger.setCronExpression("0/2 * * ? * *"); // every 2 seconds
                    scheduler.rescheduleJob(new TriggerKey("trigger"), trigger);
                    scheduler.resumeAll();
                    System.out.println("resumeAll");
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }.start();

    }
}
