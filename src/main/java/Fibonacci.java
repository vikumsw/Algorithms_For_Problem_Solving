import org.testng.Assert;
import org.testng.annotations.Test;

public class Fibonacci {
    public static int cal(int index){
        switch (index){
            case 0:
                return 0;
            case 1:
                return 1;
                default:
                    return cal(index -1) + cal(index -2);
        }

    }

    public static int calFibLoop(int index){
        switch (index){
            case 0:
                return 0;
            case 1:
                return 1;
            default:
                int valn1   = 1;
                int valn2   = 0;
                int out     = 0;

                for(int i = 1; i < index; i++){
                    out     = valn1 + valn2;
                    valn2   = valn1;
                    valn1   = out;
                }
                return out;
        }
    }

    @Test
    public void fibonacci(){
        Assert.assertEquals(3, cal(4));
        Assert.assertEquals(3, calFibLoop(4));
        Assert.assertEquals(cal(10), calFibLoop(10));
    }
}
