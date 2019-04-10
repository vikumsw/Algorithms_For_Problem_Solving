import org.testng.Assert;
import org.testng.annotations.Test;

public class InvertBinaryTree {
    class Node {
        int Value;
        Node Left = null;
        Node Right = null;

        Node (int value){
            this.Value = value;
        }
        Node SetLeft(Node left){
            this.Left = left;
            return this.Left;
        }
        Node SetRight(Node right){
            this.Right = right;
            return this.Right;
        }
    }

    private void Invert(Node root) {
        if (root != null){
            Node temp = root.Left;
            root.Left = root.Right;
            root.Right = temp;

            Invert(root.Left);
            Invert(root.Right);
        }
    }

    @Test
    public void testInvertBinaryTree(){
        Node root = new Node(10);                                        //    10
        Node L1 = root.SetLeft(new Node(5));                             //  5    15
        L1.SetLeft(new Node(1));                                         // 1 8 12 20
        L1.SetRight(new Node(8)).SetLeft(new Node(6));             //  6      22
        Node R1 = root.SetRight(new Node(15));                           //           24
        R1.SetLeft(new Node(12));
        R1.SetRight(new Node(20)).SetRight(new Node(22)).SetRight(new Node(24)).SetLeft(new Node(23));

        Invert(root);

        Assert.assertEquals(root.Right.Left.Right.Value, 6);
        Assert.assertEquals(root.Left.Value, 15);
        Assert.assertEquals(root.Right.Value, 5);
        Assert.assertEquals(root.Left.Left.Value, 20);
        Assert.assertEquals(root.Right.Right.Value, 1);
    }
}
