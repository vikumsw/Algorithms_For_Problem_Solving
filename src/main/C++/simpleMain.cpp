/*
write a template function to print a matrix 
*/

#include<iostream>
#include<vector>

using namespace std;

template<typename T>
void PrintMatrix(const vector<vector<T>>& mat){
    for(const vector<T>& r:mat){
        for(const T& v:r){
            cout<<v<<" ";
        }
        cout<<endl;
    }
    return;
}



int main(int argc, char* argv[])
{
    vector<vector<int>> mat1 = {{1,2,3},{4,5,6},{7,8,9}};
    PrintMatrix(mat1);
    vector<vector<char>> mat2 = {{'a','b','c'},{'d','e','f'},{'g','h','i'}};
    PrintMatrix(mat2);
    vector<vector<bool>> mat3 = {{true,true,true},{false,false,false},{true,true,true}};
    PrintMatrix(mat3);
    return 0;
}