class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        l = len(arr)
        while i<l:
            if arr[i]==0 and i<l-1:
                arr.insert(i+1,0)
                arr.pop()
                i+=2
            else: i +=1
