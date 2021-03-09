#include<string>
#include<iostream>
#include <assert.h> 
using namespace std;

string reverseSentence(string s){
    string rev_str = "";

    int l = s.length();

    string word = "";
    for(int i=l-1;i>-1;i--){
        if (s[i] == ' '){
            rev_str += word + ' ';
            word = "";
        }else{
            word = s[i]+ word;
        }
    }

    rev_str += word;
    return rev_str;

}


int main(){

    assert(reverseSentence("a b c")=="c b a");
    return 0;
}