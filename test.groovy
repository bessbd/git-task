import junit.framework.TestSuite
import junit.textui.TestRunner
import org.junit.Test

import java.nio.file.Files


class GitTaskSystemTest extends GroovyTestCase {

    static def runCmd(String cmd) {
        File file = File.createTempFile("temp",".sh")
        file.write cmd

        def sout = new StringBuilder(), serr = new StringBuilder()
        def proc = "bash $file.absolutePath".execute()
        proc.waitForProcessOutput(sout, serr)
        new Tuple2(sout, serr)
    }

    @Test
    void testHelp() {
        def testRepoPath = Files.createTempDirectory("testrepo")
        def (String sout, String serr) = runCmd(
                "git config --global alias.task '!'\"groovy \$(pwd)/git-task.groovy\" && " +
                "cd " + testRepoPath.toString() + " && " +
                "git init && " +
                "git task"
        )
        assertEquals "Hello hey", sout.split("\n")[1]
    }

}

TestSuite suite = new TestSuite()
suite.addTestSuite(GitTaskSystemTest)

System.exit(TestRunner.run(suite).wasSuccessful() ? 0 : 1)
