class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        lenght = len(dist)
        
        if hour < lenght - 1:
            return -1
        
        minspeed = math.ceil(sum(dist)/hour)
        print (minspeed)
            
        lo = minspeed
        hi = 10000001
        
        while lo<hi:
            s = lo + (hi - lo) // 2
            t = 0.0
            for i in range(0,lenght):
                t += math.ceil(dist[i]/s) if i != lenght-1 else float(dist[i])/float(s)
            if t<=hour:
                hi = s
            else:
                lo = s+1
        return lo              