class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n == 1: return x
        if n > 1:
            temp =  self.myPow(x, n // 2)

            if n%2 == 0: return temp * temp
            else: return temp * temp * x

        else:
            return 1 / self.myPow(x, -1 * n)

        