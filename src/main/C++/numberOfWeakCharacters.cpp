class Solution {
public:
    static bool comp(vector<int>& a,vector<int>& b){
            return (a[0]==b[0])? a[1]<b[1]:a[0]>b[0];
    }
    
    int numberOfWeakCharacters(vector<vector<int>>& properties) {
        sort(properties.begin(),properties.end(),comp);
        int max = 0;
        int count = 0;
        
        for(auto& p:properties){
            if(p[1]<max)
                count+=1;
            
            if(p[1]>max)
                max = p[1];
        }
        
        return count;
        
    }
};