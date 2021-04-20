class Solution:
    def dfs(self, dic: dict, course: int, arr: list, arrs: set, temp: set):
        if course in temp:
            return
        else:
            temp.add(course)
        
        if course in dic:
            dep = dic[course]
            if len(dep) == 0:
                arr.append(course)
                arrs.add(course)
                dic.pop(course)
            else:
                for d in dep:
                    if d not in arrs:
                        self.dfs(dic,d,arr,arrs,temp)
                
                for d in dep.copy():
                    if d in arrs:
                        dep.remove(d)
                        if len(dep) == 0:
                            arr.append(course)
                            arrs.add(course)
                            dic.pop(course)
        
    
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:        
        dic = {}
        for n in range(numCourses):
            dic[n] = []
            
        for c,p in prerequisites:
            dic[c].append(p)
        arr = []
        arrs = set()
        for x in range(numCourses):
            temp = set()
            self.dfs(dic,x,arr,arrs,temp)
        return arr if len(dic) == 0 else []

        