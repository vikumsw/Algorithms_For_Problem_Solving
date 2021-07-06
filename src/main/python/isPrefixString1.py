class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        check = ""
        for w in words:
            check +=w
            if check == s: return True
        
        return False