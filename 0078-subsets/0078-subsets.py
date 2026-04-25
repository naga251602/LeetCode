class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = pow(2, len(nums))
        res = []
        for i in range(n):
            temp = []
            k, pos = i, 0
            while k > 0:
                if k&1: temp.append(nums[pos])
                pos += 1
                k >>= 1
            res.append(temp)
        return res

            