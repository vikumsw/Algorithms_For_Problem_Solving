class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        int tot = accumulate(piles.begin(),piles.end(),0);
        priority_queue<int> mq;
        for (int &i:piles){
            mq.push(i);
        }
        
        while(k--){
            int nw = ceil(mq.top()/2.0);
            tot = tot - mq.top() + nw;
            mq.pop();
            mq.push(nw);
        }
        
        return tot;
    }
};