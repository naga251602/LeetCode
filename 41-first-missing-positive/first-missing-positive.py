class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            if nums[i] <= 0: i += 1
            else:
                pos = nums[i] - 1
                if pos < len(nums) and nums[i] != nums[pos]:
                    nums[i], nums[pos] = nums[pos], nums[i]
                else: i += 1
        
        i = 0

        while i < len(nums):
            if i+1 != nums[i]: return i + 1
            i += 1
        
        return i + 1