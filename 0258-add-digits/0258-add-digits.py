class Solution:
    def addDigits(self, num: int) -> int:
        def sum_digits(n):
            res = 0
            while n > 0:
                res += (n%10)
                n //= 10
            return res
        
        while num > 9:
            num = sum_digits(num)
        
        return num
        