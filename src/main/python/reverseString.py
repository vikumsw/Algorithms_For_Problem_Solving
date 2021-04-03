class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swap(start,end):
            if start>=end: return
            
            s[start] , s[end] = s[end] , s[start]
            swap(start+1,end-1)
        
        swap(0,len(s)-1)