class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        def getTargets(t):
            alph = "abcdefghijklmnopqrstuvwxyz"
            ind= alph.index(t)
            ll = []
            for i in range(1,26):
                ll.append(alph[(ind+i)%26])
            
            return ll
        
        def binarySearch(letters,c):
            lo = 0
            hi = len(letters)-1
            
            while lo<=hi:
                mid = lo + (hi - lo)//2
                if c== letters[mid]:
                    return True
                elif c>letters[mid]:
                    lo = mid+1
                else:
                    hi = mid-1
            
            return False
            
        
        # if target is y -> zabcdef...
        targets = getTargets(target)
        
        for c in targets:
            if binarySearch(letters,c):
                return c
                
        
        