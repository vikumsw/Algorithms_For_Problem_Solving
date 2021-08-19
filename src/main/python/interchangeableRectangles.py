class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = 0
        ratio_map = DefaultDict(int)
        for rect in rectangles:
            ratio = rect[0]/rect[1]
            ratio_map[ratio] +=1 
            
        for ratio_val in ratio_map.values():
            if ratio_val>1:
                count += math.factorial(ratio_val)/(2*math.factorial(ratio_val-2))
        
        return int(count)
