class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        lb = 0
        c = 0

        while n > 0:
            if n&1 == 0: c += 1
            else: break
            n >>= 1

        if n == 1 and c%2 == 0: return True
        return False