class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        if len(s) == 0:return True
        if len(words) == 0:return False
        
        s_ind = 0
        
        for w in words:
            for c in w:
                if s_ind==len(s) or c!=s[s_ind]:
                    return False
                else:
                    s_ind +=1
            
            if s_ind==len(s): return True
        
        return False