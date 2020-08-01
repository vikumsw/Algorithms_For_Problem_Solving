import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.Arrays;
/*
 #228:
This problem was asked by Twitter.

Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer.
For example, given [10, 7, 76, 415], you should return 77641510.
 */
public class LargestNumber {
    private Integer[] largestNumber(Integer[] data){
        Arrays.sort(data, (n1, n2) -> ("" + n2 + n1).compareTo("" + n1 + n2));
        return data;
    }

    @Test
    public void testLargestCompare(){
        Assert.assertEquals((largestNumber(new Integer[]{7, 6})), new Integer[]{7, 6});
        Assert.assertEquals((largestNumber(new Integer[]{7, 76})), new Integer[]{7, 76});
        Assert.assertEquals((largestNumber(new Integer[]{7, 78})), new Integer[]{78, 7});
        Assert.assertEquals((largestNumber(new Integer[]{10, 7, 78, 415})), new Integer[]{78, 7, 415, 10});
        Assert.assertEquals((largestNumber(new Integer[]{10, 7, 76, 415})), new Integer[]{7, 76, 415, 10});
        Assert.assertEquals((largestNumber(new Integer[]{9, 8, 99, 56, 327})), new Integer[]{9, 99, 8, 56, 327});
    }
}
