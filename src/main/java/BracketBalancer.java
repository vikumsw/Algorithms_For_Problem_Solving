import org.testng.Assert;
import org.testng.annotations.Test;
import java.util.Stack;

public class BracketBalancer {

    private static boolean IsBalanced(String input) {

        Stack<Character> myStack = new Stack();

        for(Character ch:input.toCharArray()){
            switch (ch){
                case '(':
                    myStack.push(')');
                    break;
                case '{':
                    myStack.push('}');
                    break;
                case '[':
                    myStack.push(']');
                    break;
                case ')':
                case '}':
                case ']':
                    if (myStack.pop() != ch)
                        return false;
                    break;
            }
        }

        return myStack.isEmpty();
    }

    @Test
    public void testBracketBalance(){
        Assert.assertEquals(IsBalanced("("), false);
        Assert.assertEquals(IsBalanced("{}"), true);
        Assert.assertEquals(IsBalanced("{][}"), false);
        Assert.assertEquals(IsBalanced("([])[]({})"), true);
        Assert.assertEquals(IsBalanced("([])[(]({})"), false);
        Assert.assertEquals(IsBalanced("([])[()]({})"), true);
        Assert.assertEquals(IsBalanced("([])[(])({})"), false);
    }
}
