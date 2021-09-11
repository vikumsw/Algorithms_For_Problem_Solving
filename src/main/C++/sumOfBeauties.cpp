class Solution {
public:
    int sumOfBeauties(vector<int>& nums) {
        int len = nums.size();
        vector<int> mn(len,0);
        vector<int> mx(len,0);
        
        mn[len-1]=nums[len-1];
        mx[0]=nums[0];
        
        for(int i=1;i<len;++i)
            mx[i] = max(nums[i],mx[i-1]);
        
        for(int i=len-2;i>=0;--i)
            mn[i] = min(nums[i],mn[i+1]);

        int b=0;
        for(int i=1;i<len-1;++i){
            if (mx[i-1]<nums[i] && mn[i+1]>nums[i])
                b+=2;
            else if(nums[i-1]<nums[i] && nums[i+1]>nums[i])
                b+=1;
        }
        
        
        return b;
    }
};