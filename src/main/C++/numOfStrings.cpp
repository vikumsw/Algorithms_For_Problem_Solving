class Solution {
public:
    int numOfStrings(vector<string>& patterns, string word) {
        
        int count = 0;
        for(string& w:patterns){
            if (word.find(w) != std::string::npos)
                count++;
        }
        return count;
        
    }
};