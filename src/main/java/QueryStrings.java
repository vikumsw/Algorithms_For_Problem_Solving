import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

public class QueryStrings {
    private List<String> SearchForStrings(String[] arr, String prefix) {
        List<String> ret = new ArrayList<>();
        
        for (String element : arr) {        
            if(element.substring(0, prefix.length()).equals(prefix))
                ret.add(element);      
        }
        
        return ret;
    }

    @Test
    public void testQueryString(){
        Assert.assertEquals(SearchForStrings(new String[]{"dog", "deer", "deal"}, "de"), new ArrayList<String>( Arrays.asList("deer", "deal")));
    }
}
