class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        trip = [0,0,0]
        
        def isUseful(t):
            if ( target[0] == t [0] or target[1] == t [1] or target[2] == t [2]) and (target[0] >= t [0] and target[1] >= t [1] and target[2] >= t [2]):
                return True
        
        for t in triplets:
            if isUseful(t):
                if trip[0] < t[0] :trip[0] = t[0]
                if trip[1] < t[1] :trip[1] = t[1]
                if trip[2] < t[2] :trip[2] = t[2]
            
        
        #print(trip)
        
        if trip == target:
            return True
        
        return False
