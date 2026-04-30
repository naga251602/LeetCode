class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        st, en = -1, len(nums)

        while i != en:
            if i != st and nums[i] == 0:
                nums[st+1], nums[i] = nums[i], nums[st+1]
                st += 1
            elif nums[i] == 2:
                nums[en-1], nums[i] = nums[i], nums[en - 1]
                en -= 1
            else: i += 1
        
        