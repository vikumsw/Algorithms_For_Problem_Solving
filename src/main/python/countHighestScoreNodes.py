class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        
        children = {i:[] for i in range(n)}
        
        for i,e in enumerate(parents):
            if i==0: continue
            children[e].append(i)
        
        nodeCounts = [1 for i in range(n)]
        #nodeCounts[2] = number of nodes in subtree rooted at 2
        
        def countNodes(n,nodeCounts,children):
            if len(children[n])==0:
                nodeCounts[n]=1
            else:
                for c in children[n]:
                    countNodes(c,nodeCounts,children)
                    nodeCounts[n] = nodeCounts[n] + nodeCounts[c]
            
        countNodes(0,nodeCounts,children)
        
        products = []
        for i in range(n):
            p = 1
            for c in children[i]:
                p = p*nodeCounts[c]
            
            if i!=0:
                p = p * (n-nodeCounts[i])
            
            products.append(p)
            
        return products.count(max(products))