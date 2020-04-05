import com.intellij.openapi.actionSystem.AnAction;
import com.intellij.openapi.actionSystem.AnActionEvent;
import com.intellij.openapi.actionSystem.CommonDataKeys;
import com.intellij.openapi.command.WriteCommandAction;
import com.intellij.openapi.editor.Editor;
import com.intellij.openapi.project.Project;
import com.intellij.psi.PsiElement;
import com.intellij.psi.PsiFile;
import com.intellij.psi.PsiRecursiveElementVisitor;
import com.intellij.psi.impl.source.PsiClassImpl;
import com.intellij.psi.impl.source.PsiMethodImpl;
import org.jetbrains.annotations.NotNull;

import java.util.*;

public class MethodsSorter extends AnAction {

    @Override
    public void actionPerformed(@NotNull AnActionEvent e) {
        PsiFile psiFile = e.getData(CommonDataKeys.PSI_FILE);
        if (psiFile != null) {
            Project project = e.getProject();
            Editor editor = e.getData(CommonDataKeys.EDITOR);
            if (editor != null) {
                List<PsiClassImpl> classes = collectAllClasses(psiFile);
                for (PsiClassImpl clz : classes) {
                    List<PsiMethodImpl> functions = collectAllFunctions(clz);
                    functions.sort(getTestMethodSorter());
                    WriteCommandAction.runWriteCommandAction(project,
                            () -> {
                                for (PsiElement function : functions) {
                                    PsiElement copy = function.copy();
                                    function.getParent().add(copy);
                                    function.delete();
                                }
                            }
                    );
                }
            }
        }
    }

    private List<PsiClassImpl> collectAllClasses(PsiFile psiFile) {
        List<PsiClassImpl> classes = new ArrayList<>();
        psiFile.acceptChildren(new PsiRecursiveElementVisitor() {
            @Override
            public void visitElement(PsiElement element) {
                super.visitElement(element);
                if (element instanceof PsiClassImpl) {
                    classes.add((PsiClassImpl) element);
                }
            }
        });
        return classes;
    }

    private List<PsiMethodImpl> collectAllFunctions(PsiClassImpl clz) {
        List<PsiMethodImpl> functions = new ArrayList<>();
        clz.accept(new PsiRecursiveElementVisitor() {
            @Override
            public void visitElement(PsiElement element) {
                super.visitElement(element);
                if (element instanceof PsiMethodImpl) {
                    PsiMethodImpl method = (PsiMethodImpl) element;
                    functions.add(method);
                }
            }
        });
        return functions;
    }

    private Comparator<? super PsiMethodImpl> getTestMethodSorter() {
        return (m1, m2) -> {
            boolean is1SetupMethod = Objects.requireNonNull(m1.getNameIdentifier()).getText().toLowerCase().equals("setup");
            boolean is2SetupMethod = Objects.requireNonNull(m2.getNameIdentifier()).getText().toLowerCase().equals("setup");
            boolean is1TestMethod = Arrays.stream(m1.getAnnotations()).anyMatch(a -> Objects.requireNonNull(a.getQualifiedName()).endsWith(".Test"));
            boolean is2TestMethod = Arrays.stream(m2.getAnnotations()).anyMatch(a -> Objects.requireNonNull(a.getQualifiedName()).endsWith(".Test"));
            if (is1SetupMethod) {
                return -1;
            }
            if (is2SetupMethod) {
                return 1;
            }
            if (is1TestMethod) {
                if (is2TestMethod) {
                    return Objects.requireNonNull(m1.getIdentifyingElement()).getText().compareTo(Objects.requireNonNull(m2.getIdentifyingElement()).getText());
                }
                return -1;
            }
            if (is2TestMethod) {
                return 1;
            }
            return Objects.requireNonNull(m1.getIdentifyingElement()).getText().compareTo(Objects.requireNonNull(m2.getIdentifyingElement()).getText());
        };
    }
}
