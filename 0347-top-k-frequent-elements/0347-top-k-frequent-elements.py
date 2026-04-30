class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = Counter(nums)
        b = [[] for i in range(len(nums))]
        
        for key in h: b[h.get(key)-1].append(key)
        print(b)
        res = []

        for i in range(len(nums) - 1, -1, -1):
            if k == 0: break
            
            if len(b[i]) != 0:
                for j in range(len(b[i])):
                    res.append(b[i][j])
                    k -= 1

        return res
        
        