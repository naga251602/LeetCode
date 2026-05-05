class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]

        f = bisect.bisect_left(nums, target)
        l = bisect.bisect_right(nums, target)

        if f == l: return [-1, -1]
        return [f, l-1]