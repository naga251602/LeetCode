class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st, en = 0, len(nums) - 1

        while st <= en:
            m = st + (en - st) // 2

            if nums[m] == target: return m
            elif nums[m] >= nums[st]:
                if target >= nums[st] and target < nums[m]: en = m - 1
                else: st = m + 1
            else:
                if target > nums[m] and target <= nums[en]: st = m + 1
                else: en = m - 1
        
        return -1