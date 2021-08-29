/*
Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
*/

#include<iostream>
#include<string>
using namespace std;

class Node{
    public:
        int val = 0;
        Node* next = nullptr;
        Node(int v):val(v){}
};

void print(Node* head){
    Node* n = head;
    while(n){
        cout<<n->val<<" ";
        n = n->next;
    }
    cout<<endl;

}

int sumLists(Node* h1, Node* h2){
    Node* n1 = h1;
    Node* n2 = h2;

    int carry = 0;
    int sum = 0;
    int pow = 1;
    while(n1 || n2){
        int i1 = 0;
        int i2 = 0;

        if(n1==nullptr)
            i1 = 0;
        else{
            i1 = n1->val;
            n1= n1->next;
        }

        if(n2==nullptr)
            i2 = 0;
        else{
            i2 = n2->val;
            n2 = n2->next;
        }
        
        int val = i1+i2+carry;
        sum = sum + pow * (val%10);
        carry = (val>9)?1:0;
        pow *=10; 
    }
    
    return sum;
        
}  

int main(){
    
    Node h1(7);
    Node t1(1);
    h1.next = &t1;
    Node t2(6);
    t1.next = &t2;

    Node h2(5);
    Node t3 = Node(9);
    h2.next = &t3;
    Node t4 = Node(2);
    t3.next = &t4;

    print(&h1);
    print(&h2);

    cout<<"Result is: "<<sumLists(&h1,&h2);

    
    return 0;
}