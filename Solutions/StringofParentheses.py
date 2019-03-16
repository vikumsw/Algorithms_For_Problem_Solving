'''
Challenge -> string of parentheses:
This problem was asked by Google.

Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.

'''

'''
pseudo code



openCount = 0
closeCount = 0

while c from str
    if c=='('
        openCount = openCount+1;
    else
        if openCount>0
            openCount = openCount - 1;
        else
            closeCount = closeCount - 1;

print openCount+closeCount;

'''

str= ")((())))("  #add the parenthesis string here
openCount = 0
closeCount = 0
for c in str:
    if c == '(':
        openCount += 1
    else:
        if openCount>0:
            openCount -= 1
        else:
            closeCount += 1
print("minimum number of parentheses to be removed to make the string valid :",openCount+closeCount)
    






