'''
Palindrome: Implement a function to check if a linked list is a palindrome.
'''
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
    def add(self,val):
        nw = Node(val)
        n = self
        while n.next != None:
            n = n.next
        
        n.next = nw

def printList(head:Node)-> None:
    n = head
    while n!=None:
        print(n.val, end = " ")
        n=n.next
    print()

def isPalindrome(head:Node)->bool:
    ll = []
    n = head
    while n!=None:
        ll.append(n.val)
        n=n.next
    
    s=0
    e=len(ll)-1
    while s<e:
        if ll[s]!=ll[e]:return False
        s+=1
        e-=1
    return True

if __name__ =="__main__":
    head = Node('b')
    head.add('c')
    head.add('b')
    printList(head)
    print(isPalindrome(head))
