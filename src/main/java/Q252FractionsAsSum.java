import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Q252FractionsAsSum {

    private List<Integer> FindFractions(Integer numerator, Integer Denominator){
        if (numerator == 1)
            return new ArrayList<>(Arrays.asList(Denominator));

        List<Integer> ret = new ArrayList();
        Double diff = (double) numerator/Denominator;

        while (diff > 0.000000001) {
            Double value =  Math.ceil(1/diff);
            ret.add(value.intValue());
            diff = diff - 1.0/value;
        }
        return ret;
    }

    @Test
    public void testFractionsAsSum(){
        Assert.assertEquals(FindFractions(1, 13), new ArrayList<Integer>(Arrays.asList(13)));
        Assert.assertEquals(FindFractions(4, 13), new ArrayList<Integer>(Arrays.asList(4, 18, 468)));
        Assert.assertEquals(FindFractions(7, 15), new ArrayList<Integer>(Arrays.asList(3, 8, 120)));
    }
}
