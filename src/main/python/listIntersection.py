'''
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
kth node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.
'''
import typing

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
    def add(self,nw):
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

def getIntersectingNode1(n1:Node,n2:Node)->Node:
    ids = set()
    n=n1
    while n!=None:
        ids.add(id(n))
        n=n.next
    
    print(ids)

    n = n2
    while n!=None:
        if id(n) in ids:
            print('Intersecting node found:',n.val, id(n))
            return n
        n=n.next
    
    return None

def getTailandLength(head:Node)-> typing.Tuple[Node,int] :
    n = head
    l = 0
    tail = None
    while n!=None:
        l += 1
        if n.next==None:
            tail = n
        n = n.next

    print(tail.val,l)
    return tail,l


def getIntersectingNode2(n1:Node,n2:Node)->Node:
    t1,l1 = getTailandLength(n1)
    t2,l2 = getTailandLength(n2)

    if t1 is not t2: return None

    p1 = n1
    p2 = n2
    if l1>l2:
        for i in range(l1-l2):
            p1=p1.next
    else:
        for i in range(l2-l1):
            p2=p2.next
    
    while p2!=None:
        if p1 is p2:
            print('Intersecting node found:',p1.val, id(p1))
            return p1
        p1=p1.next
        p2=p2.next

    return None




if __name__ =="__main__":
    
    common = Node(3)
    
    head = Node(1)
    head.add(Node(2))
    head.add(common)
    head.add(Node(4))
    head.add(Node(5))
    printList(head)

    head2 = Node(11)
    head2.add(common)
    printList(head2)

    print(getIntersectingNode1(head,head2).val)

    getIntersectingNode2(head,head2)



