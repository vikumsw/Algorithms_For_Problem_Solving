'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
'''

from collections import deque
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = deque()
        self.stackMin = deque()
        self.min = -1
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stackMin:
            curmin=self.stackMin[-1]
            if val<curmin:
                self.stackMin.append(val)
            else:
                self.stackMin.append(curmin)
        else:
            self.stackMin.append(val)
            
        

    def pop(self) -> None:
        self.stack.pop()
        self.stackMin.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stackMin[-1]
