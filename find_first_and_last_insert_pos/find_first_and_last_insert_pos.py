class Solution:
    def second_pos(self, nums, target):
        st, en = 0, len(nums) - 1

        while st <= en:

            m = st + (en - st) // 2

            if nums[m] == target:
                if m < len(nums) - 1 and nums[m + 1] == target: st = m + 1
                else: return m
            
            elif nums[m] < target:
                st = m + 1
            else:
                en = m - 1
        
        return -1

    def first_pos(self, nums, target):
        st, en = 0, len(nums) - 1

        while st <= en:

            m = st + (en - st) // 2

            if nums[m] == target:
                if m > 0 and nums[m - 1] == target: en = m - 1
                else: return m
            
            elif nums[m] < target:
                st = m + 1
            else:
                en = m - 1
        
        return -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.first_pos(nums, target), self.second_pos(nums, target)]