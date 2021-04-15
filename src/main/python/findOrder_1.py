class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        l = [[x,[]] for x in range(numCourses)]
       
        for p in prerequisites:
            l[p[0]][1].append(p[1])
        
        #print(l)
        
        arr = []
        
        last_len = len(l)
        cur_len  = 0
        while len(l)>0 and cur_len < last_len:
            last_len = len(l)
            for i in l:
                if(len(i[1]) == 0):
                    arr.append(i[0])
                    l.remove(i)
                else:
                    for j in range(len(i[1])):
                        if i[1][j] not in arr: break
                        if j == len(i[1]) - 1: 
                            arr.append(i[0])
                            l.remove(i)
            cur_len = len(l)

        return arr if len(l) == 0 else []