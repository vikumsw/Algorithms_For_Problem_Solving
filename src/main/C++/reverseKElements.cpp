/*
Reverse First k Elements of Queue
*/

#include<queue>
#include<iostream>
#include<stack>
using namespace std;

void showQ(queue<int> q){
    while(!q.empty())
    {
        cout<<q.front()<<' ';
        q.pop();
    }
    cout<<endl;
}

queue<int> reverseKElements(queue<int> q,int k){
    queue<int> rev_q;
    stack<int> tmp_s;
    int i = 0;
    
    while(!q.empty())
    {
        if(i<k){
            tmp_s.push(q.front());
            q.pop();

            if(i==k-1){
                while(!tmp_s.empty()){
                    rev_q.push(tmp_s.top());
                    tmp_s.pop();
                }
            }

        }
        else{
            rev_q.push(q.front());
            q.pop();
        }


        i++;
    }

    return rev_q;
}

int main(){
    queue<int> q;
    int k = 9;
    while(k--)
        q.push(9-k);
    showQ(q);
    showQ(reverseKElements(q,5));

}