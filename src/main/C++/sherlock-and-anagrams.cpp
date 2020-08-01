#include <bits/stdc++.h>

using namespace std;

bool isAnagram(string& s,int fIndex,int sIndex,int sSLen)
{
    int eLen=sSLen;
    int tempELen = sIndex - fIndex;
    if(tempELen < sSLen)
      eLen = tempELen;
    
    int s1_end=fIndex+eLen-1;
    map<char,int> s1_map;
    
    for(int i=fIndex;i<=s1_end;i++)
           s1_map[s[i]]++;
    
    int s2_start=sIndex+sSLen-eLen;
    int s2_end=sIndex+sSLen-1;
    
    for(int i=s2_start;i<=s2_end;i++)
    {
        s1_map[s[i]]--;
        if(s1_map[s[i]]<0)
            return false;
    }
    
    return true;
}





// Complete the sherlockAndAnagrams function below.
int sherlockAndAnagrams(string& s) 
{
    int count = 0;
    
    int len=s.length();
    //cout<<"Input String :"<<s<<" Length :"<<len<<endl;
    
    //Generate all Substrings
    for(int sSLen = 1;sSLen<=len-1;sSLen++)
    {
        for(int fIndex=0;fIndex<=len-sSLen-1;fIndex++)
        {
            for(int sIndex=fIndex+1;sIndex<=len-sSLen;sIndex++)
            {
                //cout<<"Substring : [F,S,L] : ["<<fIndex<<","<<sIndex<<","<<sSLen<<"]"<<endl;
                if(isAnagram(s,fIndex,sIndex,sSLen))
                    count++;
            }
        }
    }
    return count;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int q;
    cin >> q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string s;
        getline(cin, s);

        int result = sherlockAndAnagrams(s);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}
