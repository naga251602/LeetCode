class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = -1
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[pos+1] = nums[pos+1], nums[i]
                pos += 1
        
        return pos+1