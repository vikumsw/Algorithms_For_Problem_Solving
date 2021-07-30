class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        
        if arr.count(0)> 1:
            return True
        
        if 0 in arr:
            del arr[arr.index(0)]
        
        for i in arr:
            target = 2*i
            lo = 0
            hi = len(arr)-1
            while lo<=hi:
                mid = lo + (hi - lo) // 2
                if target == arr[mid]:
                    return True
                elif target < arr[mid]:
                    hi = mid - 1
                else:
                    lo = mid+1
        
        return False