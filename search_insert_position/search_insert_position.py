class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]: return 0
        if target > nums[-1]: return len(nums)

        (st, en) = (0, len(nums) - 1)

        while st <= en:
            m = st + (en - st) // 2
            if nums[m] == target: return m
            elif target > nums[m]:
                st = m + 1
            else:
                en = m - 1

        return st