import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.ArrayList;
import java.util.List;

public class IntegerPalindrome {
     private boolean IsPalindrome(int number){

       int value = number;
       int reverse = 0;

       while (value != 0){
           int mod = value % 10;
           reverse = reverse * 10 + mod;
           value = value /10;
       }
       return number == reverse;
    }

    private boolean IsPalindromeUsingList(int number){

        List<Integer> list = new ArrayList<>();
        while (number > 0) {
            list.add(number%10);
            number = number/10;
        }

        for (int i = 0; i < list.size() / 2; i++) {
            if(list.get(i) != list.get(list.size() - i -1))
                return false;
        }
        return true;
    }

    @Test
    public void TestValid(){
        Assert.assertEquals(IsPalindrome(888), true);
        Assert.assertEquals(IsPalindrome(898), true);
        Assert.assertEquals(IsPalindrome(2), true);
        Assert.assertEquals(IsPalindrome(8228), true);
        Assert.assertEquals(IsPalindrome(82328), true);
    }

    @Test
    public void TestInvalid(){
        Assert.assertEquals(IsPalindrome(889), false);
        Assert.assertEquals(IsPalindrome(899), false);
        Assert.assertEquals(IsPalindrome(21), false);
        Assert.assertEquals(IsPalindrome(8218), false);
        Assert.assertEquals(IsPalindrome(823128), false);
        Assert.assertEquals(IsPalindrome(8282), false);
    }
}
