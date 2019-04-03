import org.testng.Assert;
import org.testng.annotations.Test;

public class LargestSumNonAdjacentNumbers
{
    private int GetLargestSum(int[] arr)
    {
        int SumA = arr[0]; // Sum Including Previous element
        int SumB = 0;      // Sum Excluding Previous element
        int SumTemp;
        
        for (int i = 1; i < arr.length; i++)
        {
            SumTemp = Math.max(SumA, SumB);
            SumA = SumB + arr[i];
            SumB = SumTemp;
        }
         
        return Math.max(SumA, SumB);
    }

    @Test
    private void testLargestSum()
    {
        Assert.assertEquals(GetLargestSum(new int[]{2,4,6,2,5}), 13);
        Assert.assertEquals(GetLargestSum(new int[]{5,1,1,5}), 10);
        Assert.assertEquals(GetLargestSum(new int[]{-1,5,1,1,5,0,100,300}), 310);
        Assert.assertEquals(GetLargestSum(new int[]{-1,5,1,70,5,0,100,300}), 375);
    }
}
