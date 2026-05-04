class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0

        while i < len(nums):
            pos = nums[i] - 1
            if pos < len(nums) and nums[i] != nums[pos]:
                nums[i], nums[pos] = nums[pos], nums[i]
            else: i += 1
        
        res = []

        for i in range(1, len(nums)+1):
            if i != nums[i-1]: res.append(i)

        return res