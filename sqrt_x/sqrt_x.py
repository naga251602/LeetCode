class Solution:
    def mySqrt(self, x: int) -> int:

        if x  == 0 or x == 1: return x

        st, en = 0, x

        while st <= en:
            m = st + (en - st) // 2

            if m * m == x: return m
            elif m * m < x:
                st = m + 1
            else:
                en = m - 1
        
        return en