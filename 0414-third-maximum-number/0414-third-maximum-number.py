class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l = list(map(lambda x: -x, set(nums)))
        heapq.heapify(l)

        if len(l) < 3: return -1 * l[0]
        k = 2

        while k > 0:
            heapq.heappop(l)
            k -= 1

        return -1 * l[0]