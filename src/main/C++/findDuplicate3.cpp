class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        unordered_set<int> mem;
        for(int& n:nums){
            if (mem.find(n)!=mem.end())
                return n;
            mem.insert(n);
        }
        return 0;
    }
};