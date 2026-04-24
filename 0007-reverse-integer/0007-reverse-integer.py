class Solution:
    def reverse(self, x: int) -> int:
        u_l = (2 ** 31) - 1
        if x >= 0:
            rev = 0
            while x != 0:
                if rev >= u_l/10: return 0 
                rev = rev * 10 + (x%10)
                x //= 10
            return rev
        else:
            return -self.reverse(-x)