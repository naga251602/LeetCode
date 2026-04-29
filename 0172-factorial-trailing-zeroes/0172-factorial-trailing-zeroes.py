class Solution:
    def trailingZeroes(self, n: int) -> int:
        s = 0
        i = 5
        while i <= n:
            s += (n // i)
            i *= 5
        
        return s