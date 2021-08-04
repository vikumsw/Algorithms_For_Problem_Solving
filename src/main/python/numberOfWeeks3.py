class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        _sum, _max = sum(milestones), max(milestones)
        if 2*(_sum-_max) + 1 >= _sum:
            return _sum
        else: return 2*(_sum-_max) + 1
        