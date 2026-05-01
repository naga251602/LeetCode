class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}

        for i in range(len(nums)):
            if hm.get(nums[i], -1) != -1 and abs(i - hm.get(nums[i])) <= k: return True
            hm[nums[i]] = i
        return False
