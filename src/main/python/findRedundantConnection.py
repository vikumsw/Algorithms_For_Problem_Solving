class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # represent as a graph
        dic = collections.defaultdict(set)
        for e in edges:
            n1,n2 = e
            dic[n1].add(n2)
            dic[n2].add(n1)
        
        def dfs(s,t):
            if s not in vis:
                vis.add(s)
                if s == t:return True
                return any([dfs(c,t) for c in dic[s]])
        
        # get edges one by one from the end
        for i in range(1,len(edges)+1):
            n1,n2 = edges[-i]
            print("e=" + str(edges[-i]), end = " ")
            # remove the edge from the graph
            dic[n1].remove(n2)
            dic[n2].remove(n1)
            print("dic=" + str(dic))
            
            #perform dfs, if sucessful return true
            vis = set()
            if dfs(n1,n2):return [n1,n2]
                
            #insert edge again to dic
            dic[n1].add(n2)
            dic[n2].add(n1)
            
        
        return []
