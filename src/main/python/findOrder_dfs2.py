class Solution:
    def dfs(self, dic: dict, course: int, arr: list, arr_set: set, vis: set):
        
        if course in vis:
            vis.add(-1)
            return
    
        vis.add(course)

        #process children
        dep_arr = dic[course]
        for d in dep_arr:
            if d not in arr_set:
                self.dfs(dic,d,arr,arr_set,vis)

        #process node
        arr.append(course)
        arr_set.add(course)
    
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:        
        dic = {}
        for n in range(numCourses):
            dic[n] = []
            
        for c,p in prerequisites:
            dic[c].append(p)
            
        #print("initial dic="+str(dic))
        arr = []
        arr_set = set()
        vis = set()
        for x in range(numCourses):
            if x not in arr_set:
                self.dfs(dic,x,arr,arr_set,vis)
                if -1 in vis:
                    break
        
        return arr if -1 not in vis else []

        
