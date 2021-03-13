/*
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"
*/

#include<bits/stdc++.h>

using namespace std;

string urlify(string s1, int len)
{
    int ind1 = s1.length()-1;
    int ind2 = len-1;

    while(ind2>-1)
    {
        if(s1[ind2]==' '){
            s1[ind1] = '0';
            s1[ind1-1] = '2';
            s1[ind1-2] = '%';
            ind1 -= 3;
        }
        else
        {
            s1[ind1]=s1[ind2];
            ind1--;
        }

        ind2--;
    }

    cout<<s1<<endl;
    return s1;
}


int main()
{
    assert (urlify("Mr John Smith    ",13) == "Mr%20John%20Smith" );
    assert (urlify("Mr hello     ",9) == "Mr%20hello%20" );
    return 0;
}