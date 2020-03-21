import org.apache.commons.io.IOUtils;
import org.springframework.batch.core.StepContribution;
import org.springframework.batch.core.scope.context.ChunkContext;
import org.springframework.batch.core.step.tasklet.Tasklet;
import org.springframework.batch.repeat.RepeatStatus;

import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

public class DecompressTasklet implements Tasklet {
    private String inputResource;
    private String targetFile;

    @Override
    public RepeatStatus execute(StepContribution stepContribution, ChunkContext chunkContext) throws Exception {
        FileInputStream fis = new FileInputStream(inputResource);
        ZipInputStream zis = new ZipInputStream(new BufferedInputStream(fis));
        ZipEntry entry = zis.getNextEntry();
        FileOutputStream fos = new FileOutputStream(targetFile);
        try {
            IOUtils.copy(zis, fos);
        } finally {
            fos.flush();
            fos.close();
        }
        return RepeatStatus.FINISHED;
    }

    public String getTargetFile() {
        return targetFile;
    }

    public void setTargetFile(String targetFile) {
        this.targetFile = targetFile;
    }

    public String getInputResource() {
        return inputResource;
    }

    public void setInputResource(String inputResource) {
        this.inputResource = inputResource;
    }
}
