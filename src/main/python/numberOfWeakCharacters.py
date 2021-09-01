class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties = sorted(properties,key=lambda ele:(1/ele[0],ele[1]))
        m = 0
        count = 0
        for e in properties:
            if m>e[1]: count+=1
            m = max(m,e[1])
            
        return count