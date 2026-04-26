class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        pos = 0
        while pos < 32: 
            res <<= 1
            if n&1: res |= 1
            pos += 1
            n >>= 1
        return res