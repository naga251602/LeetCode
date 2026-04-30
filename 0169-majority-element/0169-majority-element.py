class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele, count = nums[0], 0

        for i in nums:
            if i == ele: count += 1
            else:
                if count == 0:
                    ele = i
                    count = 1
                else:
                    count -= 1

        return ele