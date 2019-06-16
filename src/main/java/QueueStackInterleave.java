import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class QueueStackInterleave {
    private void interleave(Stack<Integer> input){
        int entryCount = input.size();
        int halfSize = (entryCount + 1)/2;

        Queue<Integer> queue = new LinkedList<>();

        //Reverse first half
        for(int i = 0; i < halfSize; i++) queue.add(input.pop());
        for(int i = 0; i < halfSize; i++) input.push(queue.remove());
        for(int i = 0; i < halfSize; i++) queue.add(input.pop());
        //End reverse first half

        //To handle input with odd number of elements
        if(entryCount % 2 == 1){
            input.add(queue.remove());
            queue.add(input.pop());
        }

        for(int i = 0; i < entryCount/2; i++){
            queue.add(input.pop());
            input.add(queue.remove());
            queue.add(input.pop());
        }

        //Add data to stack.
        //This will reverse whole array providing expected result
        //First half double reversed effectively without no reverse
        //Second half only once reversed as expected.
        while (!queue.isEmpty()){
            input.add(queue.remove());
        }
    }

    private int[] testHelp(int[] in){
        Stack<Integer> input = new Stack<>();
        for(int i = in.length -1; i>=0; i--){
            input.push(in[i]);
        }
        interleave(input);

        for(int i = 0; i < in.length; i++){
            in[i] = input.pop();
        }
        return in;
    }

    @Test
    public void test(){
        Assert.assertEquals(testHelp(new int[]{1, 2, 3, 4, 5}), new int[]{1, 5, 2, 4, 3});
        Assert.assertEquals(testHelp(new int[]{10, 11, 5, 6, 3, 8}), new int[]{10, 8, 11, 3, 5, 6});
    }
}
