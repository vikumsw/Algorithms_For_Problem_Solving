class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        if 0 in arr:
            del arr[arr.index(0)]
            if 0 in arr:
                return True
        
        for i in arr:
            if 2*i in arr:
                return True
            
            
        return False