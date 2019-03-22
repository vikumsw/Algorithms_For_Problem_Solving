package C20190315;

import org.testng.Assert;
import org.testng.annotations.Test;

public class BinaryBasedDivider {
    private static int divide( int numerator, int denominator) {
        int denominatorBits = getMostSetBit(denominator);
        int numeratorBits = getMostSetBit(numerator);

        //if denominator has more bits than numerator then
        //denominator > numerator.
        if(numeratorBits < denominatorBits) return 0;

        int diffBits =  numeratorBits - denominatorBits;
        int partDivider = denominator << diffBits;

        int out = 0;
        while (diffBits-- >= 0){
            out <<= 1;
            if(numerator >= partDivider){
                out |= 1;
                numerator -= partDivider;
            }
            partDivider >>= 1;
        }

        return out;
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
        Assert.assertEquals(0, divide(2, 4));
        Assert.assertEquals(1, divide(5, 4));
        Assert.assertEquals(669, divide(2678, 4));
        Assert.assertEquals(66, divide(200, 3));
    }
}
