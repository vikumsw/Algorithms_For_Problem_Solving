import org.testng.Assert;
import org.testng.annotations.Test;

public class SquareRoot {
    int sqrt(int x)
    {
        if (x == 0 || x == 1)
            return x;

        int i = 1, ret = 1;

        while (ret <= x)
            ret = ++i * i;

        return i - 1;
    }

    @Test
    public void testSquareRoot(){
        Assert.assertEquals(sqrt(9), 3);
        Assert.assertEquals(sqrt(144), 12);
        Assert.assertEquals(sqrt(1000), 31);
    }
}


