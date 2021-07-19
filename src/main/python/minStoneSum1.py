class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        piles = list(map(lambda x:-x,piles))
        heapq.heapify(piles)
        
        for _ in range(k):
            mx = -1*heapq.heappop(piles)
            newVal=math.ceil(mx/2)
            heapq.heappush(piles, -1*newVal)
            
        return -1* sum(piles)