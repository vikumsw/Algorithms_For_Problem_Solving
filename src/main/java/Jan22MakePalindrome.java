import org.testng.Assert;
import org.testng.annotations.Test;

public class Jan22MakePalindrome {

    private static String MakePalindrome(String input) {

        if (IsPalindrome(input))
            return input;

        Character a = input.charAt(0);
        Character b = input.charAt(input.length()-1);

        if (a == b)
            return (a + MakePalindrome(input.substring(1, input.length()-1)) + b);
        else {
            String One = a + MakePalindrome(input.substring(1)) + a;
            String Two = b + MakePalindrome(input.substring(0, input.length()-1)) + b;

            if (One.length() < Two.length())
                return One;
            else if (One.length() > Two.length())
                return Two;
            else
                return One.compareTo(Two) < 0 ? One : Two;
        }
    }

    private static Boolean IsPalindrome(String input){
        return input.equals(new StringBuilder(input).reverse().toString());
    }


    @Test
    public void testMakePalindrome(){
        Assert.assertEquals(MakePalindrome("race"), "ecarace");
        Assert.assertEquals(MakePalindrome("google"), "elgoogle");
        Assert.assertEquals(MakePalindrome("gooele"), "gooeleoog");
        Assert.assertEquals(MakePalindrome("oele"), "oeleo");
        Assert.assertEquals(MakePalindrome("oaelo"), "oaeleao");
        Assert.assertEquals(MakePalindrome("oilvwx"), "oilvwxwvlio");
    }
}