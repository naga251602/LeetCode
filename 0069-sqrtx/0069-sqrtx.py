class Solution:
    def mySqrt(self, x: int) -> int:
        st, en = 1, x

        while st <= en:
            m = (st + en) // 2
            if m * m == x: return m
            elif m * m < x: st = m + 1
            else: en = m - 1
        
        return en