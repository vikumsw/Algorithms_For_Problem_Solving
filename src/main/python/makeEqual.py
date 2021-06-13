class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = collections.defaultdict(int)
        l = len(words)
        for w in words:
            for c in w:
                d[c] = d[c]+1
        
        for c in d:
            if d[c]%l!=0:return False

        
        return True
