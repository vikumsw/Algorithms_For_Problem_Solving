import org.testng.Assert;
import org.testng.annotations.Test;

public class Fibonacci {
    public static int cal(int index) {
        switch (index) {
            case 0:
                return 0;
            case 1:
                return 1;
            default:
                return cal(index - 1) + cal(index - 2);
        }

    }

    public static int calFibLoop(int index) {
            int valn1 = 0;
            int valn2 = 1;
            for (int i = 0; i < index; i++) {
                int out = valn1 + valn2;
                valn2 = valn1;
                valn1 = out;
            }
            return valn1;
    }

    @Test
    public void fibonacci() {
        Assert.assertEquals(3, cal(4));
        Assert.assertEquals(2, calFibLoop(3));
        Assert.assertEquals(3, calFibLoop(4));
        Assert.assertEquals(cal(10), calFibLoop(10));
    }
}
