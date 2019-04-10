import org.testng.Assert;
import org.testng.annotations.Test;

import static java.lang.Character.isDigit;

public class StringCountEncodeDecoder {

    private String Encode(String input) {
        String ans = "";
        char pre = input.charAt(0);
        int count = 1;
        for (int i = 1; i < input.length(); i++) {
            if (pre == input.charAt(i)) {
                count++;
            }else {
                ans = ans + count + pre;
                pre = input.charAt(i);
                count = 1;
            }
        }
        return (ans + count + pre);
    }

    private String Decode(String input) {
        String ans = "";
        int tempIdx = 0;
        for (int i = 0; i < input.length(); i++) {
            if (!isDigit(input.charAt(i))){
                int n = Integer.parseInt(input.substring(tempIdx, i));
                ans = ans + new String(new char[n]).replace("\0", (""+input.charAt(i)));
                tempIdx = i + 1;
            }
        }
        return ans;
    }

    @Test
    public void testEncode(){
        Assert.assertEquals(Encode("AAAABBBCCDAA"), "4A3B2C1D2A");
    }

    @Test
    public void testDecode(){
        Assert.assertEquals(Decode("11A3B2C1D2A"), "AAAAAAAAAAABBBCCDAA");
    }
}