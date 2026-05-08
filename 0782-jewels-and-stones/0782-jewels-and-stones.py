class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = [0] * 26
        cap = [0] * 26

        for i in range(len(jewels)):
            if jewels[i].isupper(): cap[ord(jewels[i]) - 65] += 1
            else: c[ord(jewels[i]) - 97] += 1
        
        count = 0

        for i in range(len(stones)):
            if (stones[i].isupper() and cap[ord(stones[i]) - 65] > 0) or (stones[i].islower() and c[ord(stones[i]) - 97] > 0): count += 1
            
        
        return count