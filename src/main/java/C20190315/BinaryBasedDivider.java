package C20190315;

import org.testng.Assert;
import org.testng.annotations.Test;

public class BinaryBasedDivider {
    private static int divide( int numerator, int denominator) {
        int denominatorBits = getMostSetBit(denominator);
        int numeratorBits = getMostSetBit(numerator);

        int diffBits =  numeratorBits - denominatorBits;

        int remaining = numerator;
        int result = 0;
        int iterateCount = diffBits;
        int term = denominator << diffBits;

        while (iterateCount-- >= 0){
            result <<= 1;
            if(remaining >= term){
                result |= 1;
                remaining -= term;
            }
            term >>= 1;
        }

        return result;
    }

    private static int getMostSetBit(int value){
        int bit = 0;

        while (value != 0){
            bit++;
            value >>= 1;
        }

        return bit;
    }

    @Test
    public void testDivide(){
        Assert.assertEquals(divide(2, 4), 0);
        Assert.assertEquals(divide(5, 4), 1);
        Assert.assertEquals(divide(2678, 4), 669);
        Assert.assertEquals(divide(200, 3), 66);
    }
}
