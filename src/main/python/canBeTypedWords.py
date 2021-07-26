class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        brokenLetterSet = set(brokenLetters)
        
        def canWrite(word):
            for ch in word:
                if ch in brokenLetterSet:
                    return False
            
            return True
        
        count = 0 
        words = text.split()
        print(words)
        
        for word in words:
            if canWrite(word):
                count +=1
        
        return count
                
        
