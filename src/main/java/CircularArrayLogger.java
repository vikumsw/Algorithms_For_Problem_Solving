import org.testng.Assert;
import org.testng.annotations.Test;
import java.util.stream.Stream;

public class CircularArrayLogger {
    
    class CircularArray{
        String arr[];
        int size;
        int nextIndex = 0;
        
        CircularArray(int iSize){
            arr = new String[iSize];
            size = iSize;
        }        
        void record(String order_id){
            arr[nextIndex] = order_id;
            nextIndex = (nextIndex+1)%size;
        }       
        String get_last(int i) {
            int ithLastIndex = (nextIndex + size - i) % size;
            return arr[ithLastIndex];
        }
    }

    @Test
    public void testCircularLogger(){

        CircularArray myArr = new CircularArray(6);

        myArr.record("order001"); myArr.record("order002"); myArr.record("order003");
        myArr.record("order004"); myArr.record("order005"); myArr.record("order006");
        myArr.record("order007"); myArr.record("order008"); myArr.record("order009");
        myArr.record("order010"); myArr.record("order011");

        Assert.assertEquals(myArr.get_last(3), "order009");
        Assert.assertEquals(myArr.get_last(6), "order006");

        Stream.of("order0012", "order013", "order014", "order015").forEach(myArr::record);

        Assert.assertEquals(myArr.get_last(3), "order013");
        Assert.assertEquals(myArr.get_last(6), "order010");
    }
}