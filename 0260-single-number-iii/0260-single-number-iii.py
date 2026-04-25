class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = 0
        for i in nums: res ^= i

        k, temp = 0, res

        while temp&1 != 1:
            k += 1
            temp >>= 1
        
        num_1, num_2 = res, res

        for i in nums:
            if (i >> (k))&1: num_1 ^= i
            else: num_2 ^= i
        
        return [num_1, num_2]
        