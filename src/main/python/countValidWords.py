class Solution:
    def countValidWords(self, sentence: str) -> int:
        
        
        def valid(s):
            hc = 0
            pc = 0
            for i,c in enumerate(s):
                if ord('0')<=ord(c)<=ord('9'): return False
                
                if c == '-':
                    hc = hc+1
                    if hc>1: return False
                    
                    if not ord('a')<=ord(s[i-1])<=ord('z'): return False
                    if i+1<len(s) and not ord('a')<=ord(s[i+1])<=ord('z'): return False
                
                if c in '!.,':
                    pc = pc + 1
                    if pc>1: return False
            
            if s[0]=='-' or s[-1]=='-': return False
            if pc==1 and s[-1] not in '!.,': return False
            
            return True
        
        tokens = sentence.split()
        print(tokens)
        count = 0
        for t in tokens:
            if valid(t): 
                count = count+1
                print('valid:',t)
                
        return count