class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        nums.sort()
        l = len(nums)
        if l<3:
            return nums
        if l==3:
            temp = nums[1]
            nums[1] = nums[2]
            nums[2] = temp
            return nums
        
        ind = 1
        first_Middle = nums[1]
        
        while ind<l:
            if ind+2 < l:
                nums[ind] = nums[ind+2]
            else:
                nums[ind] = first_Middle
                if (nums[ind-2]+nums[ind])/2.0 == nums[ind-1]:
                    if ind+1<l:
                        nums[ind] = nums[ind+1]
                        nums[ind+1] = first_Middle
                    else:
                        nums[ind] = nums[0]
                        nums[0] = first_Middle
                break
            
            ind = ind + 2
        return nums