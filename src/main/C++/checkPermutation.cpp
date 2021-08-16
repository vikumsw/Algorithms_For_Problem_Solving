#include<bits/stdc++.h>

using namespace std;

bool checkPermutation(string s1, string s2)
{
    sort(s1.begin(),s1.end());
    sort(s2.begin(),s2.end());

    return s1 == s2;
}

bool checkPermutation2(string s1,string s2)
{
    if (s1.length()!=s2.length())
        return false;

    map<char,int> mem;
    for (auto& c:s1)
        mem[c] +=1;

    for (auto& c:s2){
        if(mem[c]==0)
            return false;
        else
            mem[c] -= 1;
    }

    return true;

}

int main()
{
    assert ( checkPermutation("abcd","dacb") == true );
    assert ( checkPermutation("abcd","dacbe") == false );
    assert ( checkPermutation("abcd","da") == false );

    assert ( checkPermutation2("abcd","dacb") == true );
    assert ( checkPermutation2("abcd","dacbe") == false );
    assert ( checkPermutation2("abcd","da") == false );
    return 0;
}