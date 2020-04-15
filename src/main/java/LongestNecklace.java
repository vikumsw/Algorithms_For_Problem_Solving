import org.testng.Assert;
import org.testng.annotations.Test;
import java.util.Arrays;

public class LongestNecklace {
    public int solution(int[] A) {
        if (A.length <= 0)
            return 0;

        int[] beads = new int[A.length + 1];
        int index = 0;
        int head;
        int tail;
        int count;
        int max = 0;

        for (int i = 0; i < A.length; i++) {
            count = 1;
            head = i;
            tail = A[i];
            if (head != tail) {
                if (!Arrays.asList(beads).contains(head) || head == 0) {
                    beads[index++] = head;
                    beads[index] = tail;
                    while (head != tail) {
                        tail = A[tail];
                        beads[index] = tail;
                        count++;
                    }
                }
            }

            if (count > max) max = count;
        }
        return max;
    }

    @Test
    public void test() {
        int[] testArray = {5, 4, 0, 3, 1, 6, 2};
        Assert.assertEquals(solution(testArray), 4);
    }
}
