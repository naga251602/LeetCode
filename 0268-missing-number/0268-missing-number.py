class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            pos = nums[i]
            if pos < len(nums) and nums[i] != nums[pos]: 
                nums[i], nums[pos] = nums[pos], nums[i]
            else: i += 1

        for i in range(len(nums)):
            if i != nums[i]: return i
        return i+1
        