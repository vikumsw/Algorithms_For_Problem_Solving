/*
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
*/


int returnKth2Last(Node* head,int k){
    Node* p1 = head;
    Node* p2 = head;

    while(k--)
    {
        if(p2==nullptr)
            return -1;
        p2=p2->next;
    }

    while(p2->next!=nullptr){
        p1=p1->next;
        p2=p2->next;
    }

    return p1->val;
}