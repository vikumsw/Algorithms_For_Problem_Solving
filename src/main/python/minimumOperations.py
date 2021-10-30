class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        ss = set()
        ss.add(start)
        
        steps = 0
        processed = set()
        
        
        while len(ss)>0:
            steps += 1
            #print(ss)
            
            tempss = set()
            for x in ss:
                if x in processed:
                    continue
                    
                for e in nums:
                    op = x + e
                    if op == goal:
                        return steps
                    else:
                        if 0<=op<=1000:
                            tempss.add(op)


                    op = x - e
                    if op == goal:
                        return steps
                    else:
                        if 0<=op<=1000:
                            tempss.add(op)


                    op = x ^ e
                    if op == goal:
                        return steps
                    else:
                        if 0<=op<=1000:
                            tempss.add(op)
                    
                processed.add(x)
            
            ss = tempss
            
        
        return -1
            
        