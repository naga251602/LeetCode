class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0: return 0
        
        count = 0
        s.sort()
        g.sort()
        
        i, j = 0, 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                j += 1
                count += 1
            else:
                j += 1
        
        return count