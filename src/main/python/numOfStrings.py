class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for w in patterns:
            if w in word: count +=1
        
        return count