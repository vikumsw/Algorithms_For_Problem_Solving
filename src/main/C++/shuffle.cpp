/*
16. Shuffle an Array of Integers
“Given an integer array of size n, create a program to recursively shuffle the array so no two elements remain next to each other. Do not use extra space in your solution.”
*/

#include<vector>
#include<iostream>

using namespace std;

void shuffle(vector<int>& vec,int s)
{
    int size = vec.size()-1-s+1;
    if (size < 3){
        return;
    }

    //shuffle first two
    int mid = s + (size + 1)/2;
    int temp = vec[mid];

    for (int i=mid;i>=s+2;i--) 
        vec[i] = vec[i-1];

    vec[s+1] = temp;

    shuffle(vec,s+2);
}

void print(vector<int> vec){
    for(auto&ei:vec)
            cout<<ei<<" ";
        cout<<endl;
    return;
}

int main()
{
    vector<vector<int>> vec = {{1,3,5,2,4,6},{1,2,3},{1,2},{},{1,2,3,4,5}};
    
    cout<< vec[3].size()<<endl;

    for(auto& e:vec){
        cout<<"Start..."<<endl;
        print(e);
        shuffle(e,0);
        print(e);
        cout<<"End..."<<endl;
    }
    
    return 0;
}