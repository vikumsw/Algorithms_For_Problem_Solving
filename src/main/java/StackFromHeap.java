import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.*;

public class StackFromHeap {
    private static class Heap<T extends Comparable> {
        TreeSet<T> treeSet = new TreeSet<>();
        void push(T data){
            treeSet.add(data);
        }

        T pop(){
            T data = null;
            if(!treeSet.isEmpty()){
                data = treeSet.last();
                treeSet.remove(data);
            }
            return data;
        }
    }

    private static class StackElement<T> implements Comparable<StackElement>{
        Integer index;
        T data;

        StackElement(Integer index, T data){
            this.index = index;
            this.data = data;
        }

        @Override
        public int compareTo(StackElement o) {
            return this.index.compareTo(o.index);
        }
    }

    private static class Stack<T> {
        int count = 0;
        Heap<StackElement<T>> heap = new Heap<>();
        void push(T data){
            count++;
            StackElement<T> element = new StackElement<>(count, data);
            heap.push(element);
        }

        T pop(){
            if(count > 0){
                count--;
                return heap.pop().data;
            }
            return null;
        }
    }

    @Test
    public void heapTest(){
        Heap<Integer> heap = new Heap<>();
        heap.push(3);
        heap.push(5);
        heap.push(2);

        Assert.assertEquals(heap.pop().intValue(), 5);
        Assert.assertEquals(heap.pop().intValue(), 3);
        Assert.assertEquals(heap.pop().intValue(), 2);
        Assert.assertNull(heap.pop());
    }

    @Test void stackTest(){
        Stack<String> stringStack = new Stack<>();
        stringStack.push("Test1");
        stringStack.push("Test2");
        stringStack.push("Test3");

        Assert.assertEquals(stringStack.pop(), "Test3");

        stringStack.push("Test4");
        Assert.assertEquals(stringStack.pop(), "Test4");
        Assert.assertEquals(stringStack.pop(), "Test2");
        Assert.assertEquals(stringStack.pop(), "Test1");
        Assert.assertNull(stringStack.pop());

    }
}
