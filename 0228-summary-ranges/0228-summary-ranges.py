class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0: return []
        st = nums[0]
        en = nums[0]
        res = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1: 
                en = nums[i]
            else:
                if st == en: res.append(f'{st}')
                else: res.append(f'{st}->{en}')
                st = nums[i]
                en = nums[i]
        
        if st == en: res.append(f'{st}')
        else: res.append(f'{st}->{en}')
        return res