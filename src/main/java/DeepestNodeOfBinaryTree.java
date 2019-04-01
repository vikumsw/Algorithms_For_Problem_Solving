
public class DeepestNodeOfBinaryTree {

    static private int deepestLevel;
    static private int deepestValue;
    static class Node {
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

    public static void main(String[] args) {
        Node root = new Node(10);
        Node L1 = root.SetLeft(new Node(5));
        L1.SetLeft(new Node(1));
        L1.SetRight(new Node(8)).SetLeft(new Node(6));
        System.out.println("Deepest Node: " + GetDeepestNode(root));
        Node R1 = root.SetRight(new Node(15));
        R1.SetLeft(new Node(12));
        R1.SetRight(new Node(20)).SetRight(new Node(22)).SetRight(new Node(24)).SetLeft(new Node(23));
        System.out.println("Deepest Node: " + GetDeepestNode(root));
    }

    private static int GetDeepestNode(Node root) {
        Find(root, 0);
        return deepestValue;
    }

    private static void Find(Node root, int level)
    {
        if (root != null){
            Find(root.Left, ++level);
            if (level > deepestLevel){
                deepestLevel = level;
                deepestValue = root.Value;
            }
            Find(root.Right, level);
        }
    }
}
