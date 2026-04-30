class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        st, en = 0, len(nums) - 1

        while st <= en:
            m = st + (en - st) // 2
            if nums[m] == target: return m
            elif nums[m] < target: st = m + 1
            else: en = m - 1
        
        return en+1