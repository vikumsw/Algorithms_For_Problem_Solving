/*
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
*/

class ValidParanthesis {
    
    private void solveParanthesis(Stack<Character> stack, int index, String s,int length)
    {
        if(length-1 < index)
            return;
        char cur = s.charAt(index);
        
        if(!stack.empty())
        {
            char top = stack.peek();
            boolean closes = false;
            closes = (top=='(' && cur == ')') || (top=='{' && cur == '}')||(top=='[' && cur == ']');

            if(closes)
                stack.pop();
            else
                stack.push(cur);
        }
        else
            stack.push(cur);

        solveParanthesis(stack,index+1,s,length);
    }
    
    public boolean isValid(String s) {
        
        Stack<Character> stack = new Stack<>();
        solveParanthesis(stack,0,s,s.length());
        if (stack.empty())
            return true;
        
        return false;
    }
}
