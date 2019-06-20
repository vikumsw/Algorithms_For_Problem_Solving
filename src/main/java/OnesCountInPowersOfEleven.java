import org.testng.Assert;
import org.testng.annotations.Test;

public class OnesCountInPowersOfEleven {
    private int NumberOfOnes(int n) {

        if (n == 0)
            return 1;

        int len = 2000;
        byte[] digits = new byte[len];
        byte[] temp = new byte[len];

        digits[0] = 1;
        digits[1] = 1;

        for(int p = 1; p < n ; p++){
            for(int num = 0; num < len; num++){
                temp[num] = digits[num];
            }

            for(int num = len - 2; num >=0; num--){
                digits[num + 1] = digits[num];
            }
            digits[0] = 0;

            byte carry = 0;
            for(int num = 0; num < len; num++){
                int out = digits[num] + temp[num] + carry;
                if(out >= 10){
                    digits[num] =(byte)(out -10);
                    carry = 1;
                } else {
                    digits[num] = (byte)out;
                    carry = 0;
                }
            }
        }

        int ones = 0;
        for(int num = 0; num < len; num++){
            if(digits[num] == 1){
                ones++;
            }
        }
        return ones;
    }

    @Test
    public void testEncode(){
        Assert.assertEquals(NumberOfOnes(0), 1);
        Assert.assertEquals(NumberOfOnes(11), 4);
        Assert.assertEquals(NumberOfOnes(12), 2);
        Assert.assertEquals(NumberOfOnes(1000), 105);
        Assert.assertEquals(NumberOfOnes(100), 12);
    }
}
