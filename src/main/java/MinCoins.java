import org.testng.Assert;
import org.testng.annotations.Test;

public class MinCoins {
    private static int[] coinValues = {1, 5, 10, 25};
    private static int minCoins(int value){
        int coinCount = 0;
        for(int valIndex = coinValues.length - 1; valIndex>= 0; valIndex--){
            coinCount += value/coinValues[valIndex];
            value = value % coinValues[valIndex];
        }
        return coinCount;
    }

    @Test
    public void tests(){
        Assert.assertEquals(minCoins(16), 3);
        Assert.assertEquals(minCoins(26), 2);
        Assert.assertEquals(minCoins(19), 6);
    }
}
