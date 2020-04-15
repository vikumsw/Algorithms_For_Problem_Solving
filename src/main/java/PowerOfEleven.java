import org.testng.Assert;
import org.testng.annotations.Test;
import java.util.stream.IntStream;

public class PowerOfEleven {
    public int solution(int N) {
        if (N == 0)
            return 1;

        int len = 1500;
        byte[] numbs = new byte[len];
        byte[] temp = new byte[len];

        numbs[0] = 1;
        numbs[1] = 1;

        for(int i = 1; i < N ; i++){
            System.arraycopy(numbs, 0, temp, 0, len);
            System.arraycopy(numbs, 0, numbs, 1, len - 2 + 1);
            numbs[0] = 0;
            byte carry = 0;
            for(int num = 0; num < len; num++){
                int out = numbs[num] + temp[num] + carry;
                if(out >= 10){
                    numbs[num] = (byte)(out - 10);
                    carry = 1;
                } else {
                    numbs[num] = (byte)out;
                    carry = 0;
                }
            }
        }

        int count = (int) IntStream.range(0, len).filter(num -> numbs[num] == 1).count();
        return count;
    }

    @Test
    public void test() {
        Assert.assertEquals(solution(0), 1);
        Assert.assertEquals(solution(1), 2);
        Assert.assertEquals(solution(3), 2);
        Assert.assertEquals(solution(8), 2);
        Assert.assertEquals(solution(11), 4);
        Assert.assertEquals(solution(12), 2);
        Assert.assertEquals(solution(1000), 105);
    }
}
