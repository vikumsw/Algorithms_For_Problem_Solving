/*
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
*/
#include<vector>
#include<iostream>
#include<set>

using namespace std;

void makeZero(vector<vector<int>>& mat,int i,bool is_column){
    int row_count = mat.size();
    int col_count = mat[0].size();

    if(is_column){
        for(int r=0;r<row_count;r++){
            mat[r][i] = 0;
        }
    }
    else
    {
        for(int c=0;c<col_count;c++){
            mat[i][c] = 0;
        }
    }
    return;
}


void zeroMatrix(vector<vector<int>>& mat)
{
    int row_count = mat.size();
    if(row_count==0) return;
    int col_count = mat[0].size();

    set<int> rows;
    set<int> cols;
    for(int r=0;r<row_count;r++){
        for(int c=0;c<col_count;c++){
            if(mat[r][c]==0){
                rows.insert(r);
                cols.insert(c);
            }
        }
    }

    for(auto& i:rows){
        makeZero(mat,i,false);
    }

    for(auto& i:cols){
        makeZero(mat,i,true);
    }
}

void printMat(vector<vector<int>>& mat){
    int row_count = mat.size();
    int col_count = mat[0].size();
    for(int r=0;r<row_count;r++){
        for(int c=0;c<col_count;c++){
            cout<<mat[r][c]<<" ";
        }
        cout<<endl;
    }
}


int main(){
    vector<vector<int>> mat={{1,2,0},{4,9,6},{7,8,9},{6,0,5}};
    zeroMatrix(mat);
    printMat(mat);

    return 0;
}