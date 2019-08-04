/*
Challenge #228:
This problem was asked by Twitter.

Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer.
For example, given [10, 7, 76, 415], you should return 77641510
 */

import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.ArrayList;
import java.util.List;

public class Q228LargestInteger {
    private class Node {
        private Node left;
        private Node right;
        private int value;
        private Node(int value){
            left = right = null;
            this.value = value;
        }
    }

    private class Tree {
        private Node root;

        private void insert(int value) {
            if (root == null){
                root = new Node(value);
                return;
            }
            root = insert(root, value);
        }

        private Node insert(Node root, int value){
            if (root == null)
                return new Node(value);

            int side = getSide(root.value, value);
            if (side == 1)
                root.right = insert(root.right, value);
            else
                root.left = insert(root.left, value);

            return root;
        }

        private int getSide(int root, int value){
            String s1 = Integer.toString(root);
            String s2 = Integer.toString(value);
            Integer i1 = Integer.parseInt(s1+s2);
            Integer i2 = Integer.parseInt(s2+s1);
            return i2.compareTo(i1);
        }

        private void traverseTree(Node root, List<Integer> integers){
            if (root == null)
                return;

            traverseTree(root.right, integers);
            integers.add(root.value);
            traverseTree(root.left, integers);
        }
    }

    private String getMaxInt(int[] numbers){
        Tree integerTree = new Tree();
        for(int number : numbers)
            integerTree.insert(number);

        List<Integer> sortedIntegers = new ArrayList<>();
        integerTree.traverseTree(integerTree.root, sortedIntegers);

        StringBuilder maxInteger = new StringBuilder();
        for (int number : sortedIntegers){
            maxInteger.append(number);
        }
        return maxInteger.toString();
    }

    @Test
    public void testMaxInt(){
        int [] numbers = {9, 8, 56, 99, 327};
        int [] numbers1 = {12, 9, 8, 56, 89, 327};
        int [] numbers2 = {10, 7, 76, 415};
        int [] numbers3 = {10, 7, 78, 415};

        Assert.assertEquals(getMaxInt(numbers), "999856327");
        Assert.assertEquals(getMaxInt(numbers1), "98985632712");
        Assert.assertEquals(getMaxInt(numbers2), "77641510");
        Assert.assertEquals(getMaxInt(numbers3), "78741510");
    }
}
