class Solution {
public:
    bool isPrefixString(string s, vector<string>& words) {
        int ind = 0;
        
        for(auto &w: words){
            for(auto &c: w){
                if(ind>s.size()-1 || c!=s[ind])
                    return false;
                else
                    ind +=1;
            }
            
            if (ind == s.size())
                return true;
                
            
        }
        
        return false;
        
    }
};