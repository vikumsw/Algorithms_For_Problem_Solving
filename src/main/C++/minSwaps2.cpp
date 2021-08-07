class Solution {
public:
    int minSwaps(string s) {
        int c1=0;
        int c2=0;
    
        for(auto& c:s){
            if (c=='[') c1++;
            else
            {
                if(c1==0) c2++;
                else c1--; 
            }
                
        }
        
        return (c1+1)/2;
        
    }
};