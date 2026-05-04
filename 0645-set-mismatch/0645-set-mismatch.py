class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0

        while i < len(nums):
            pos = nums[i] - 1
            if pos < len(nums) and nums[pos] != nums[i]:
                nums[i], nums[pos] = nums[pos], nums[i]
           
            else: i += 1
        
        print(nums)
        for i in range(1, len(nums)):
            if i != nums[i-1]: return [nums[i-1], i]
        
        return [nums[-1], i+1]