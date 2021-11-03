class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target<letters[0]:
            return letters[0]
        
        if target>=letters[-1]:
            return letters[0]
        
        hi = len(letters)-1
        lo = 1
        
        while hi>=lo:
            mid = lo + (hi-lo)//2
            
            if letters[mid]>target and letters[mid-1]<=target:
                return letters[mid]
            elif letters[mid] <= target:
                lo = mid+1
            else:
                hi = mid-1