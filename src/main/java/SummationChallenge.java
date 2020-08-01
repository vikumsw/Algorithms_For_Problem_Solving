import org.testng.Assert;
import org.testng.annotations.Test;

public class SummationChallenge {
    public int solution(int N) {
        if (N == 0)
            return 0;
        else if (N == 1)
            return 1;
        else if (N > 27)
            return getSummation(N % 24 + 24);

        return getSummation(N);
    }

    private int getSummation(int N){
        int val_0 = 0;
        int val_1 = 1;
        for (int i = 2; i <= N; i++) {
            int val_i = getDigitSum(val_0) + getDigitSum(val_1);
            val_0 = val_1;
            val_1 = val_i;
        }

        return val_1;
    }

    private int getDigitSum(int num)
    {
        return num == 0 ? 0 : num % 10 + getDigitSum(num/10) ;
    }

    @Test
    public void test() {
        Assert.assertEquals(solution(0), 0);
        Assert.assertEquals(solution(1), 1);
        Assert.assertEquals(solution(2), 1);
        Assert.assertEquals(solution(6),8);
        Assert.assertEquals(solution(10),10);
        Assert.assertEquals(solution(12),9);
        Assert.assertEquals(solution(100),3);
        Assert.assertEquals(solution(1000),15);
        Assert.assertEquals(solution(10000),15);
        Assert.assertEquals(solution(24),9);
        Assert.assertEquals(solution(24),9);
        Assert.assertEquals(getSummation(48),9);
        Assert.assertEquals(solution(48),9);
    }
}
