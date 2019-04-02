import org.testng.Assert;
import org.testng.annotations.Test;

public class StepsCombinations
{
    private int GetCombinations(int N, int[] arrPossibleClimbs)
    {
        int iComb = 0;
        for (int element : arrPossibleClimbs) {
            if (element < N) 
                iComb += GetCombinations(N-element, arrPossibleClimbs);
            else if (element == N)
                iComb++;
        }
        return iComb;
    }

    @Test
    public void testCombinations()
    {
        Assert.assertEquals(GetCombinations(4, new int[] {1,2}), 5);
        Assert.assertEquals(GetCombinations(7, new int[] {1,3,5}), 12);
        Assert.assertEquals(GetCombinations(8, new int[] {1,2,3,4}), 108);
        Assert.assertEquals(GetCombinations(9, new int[] {2,4,6,9}), 1);
        Assert.assertEquals(GetCombinations(10, new int[] {2,4,6,10}), 14);
        Assert.assertEquals(GetCombinations(9, new int[] {2,3,6,9}), 8);
    }
}