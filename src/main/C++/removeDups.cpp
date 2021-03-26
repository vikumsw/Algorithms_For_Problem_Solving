/*
Remove Dups: Write code to remove duplicates from an unsorted linked list.
*/
#include<iostream>
#include<set>

using namespace std;

class Node{
    public:
        int val = 0;
        Node* next = nullptr; 

        Node(int a):val(a),next(nullptr){
            //cout<<"calling cons "<<a<<endl;
        }
        ~Node(){
            delete this->next;
        }

        Node& add(int a){
            Node* nw = new Node(a);

            Node* n = this;

            while(n->next != nullptr){
                n = n->next;
            } 
            n->next = nw;

            return *this;
        }

        void print(){
            Node* n = this;
            cout<<"Printing : ";
            while(n!=nullptr){
                cout<<n->val<<" ";
                n = n->next;
            }
            cout<<endl;
        }

};

void removeDuplicates(Node* head){
    set<int> memo;
    Node* prev = nullptr;
    Node* n = head;
    while(n!=nullptr){
        if(memo.find(n->val)!=memo.end())
        {
            prev->next = n->next;
            n->next = nullptr;
            delete n;
            n = prev->next;
        }
        else
        {
            memo.insert(n->val);
            prev = n;
            n = n->next; 
        }
    }
}

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

int main(){

    cout<<"starting"<<endl;

    Node* head = new Node(10);
    (*head).add(5).add(6).add(7).add(90).add(20).add(8).add(7).add(89).add(10);
    head->print();

    cout<< "3rd to last element is:"<< returnKth2Last(head,3)<<endl;
    cout<< "5th to last element is:"<< returnKth2Last(head,5)<<endl;
    cout<< "20th to last element is:"<< returnKth2Last(head,20)<<endl;

    removeDuplicates(head);
    head->print();
    cout<<"finished"<<endl;

}

