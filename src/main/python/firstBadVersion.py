# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        lo = 1
        hi = n
        while lo<=hi:
            mid = lo + (hi - lo) // 2
            if mid >1:
                if isBadVersion(mid) and not isBadVersion(mid-1):
                    return mid
                elif isBadVersion(mid) and isBadVersion(mid-1):
                    hi = mid - 1
                elif not isBadVersion(mid) and not isBadVersion(mid-1):
                    lo = mid+1
            elif mid == 1:
                if not isBadVersion(mid):
                    lo = mid+1
                if isBadVersion(mid):
                    return 1
        return -1