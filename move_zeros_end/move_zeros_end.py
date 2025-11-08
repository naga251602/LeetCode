class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = -1

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos + 1], nums[i] = nums[i], nums[pos + 1]
                pos += 1