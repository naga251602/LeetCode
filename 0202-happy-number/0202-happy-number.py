class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(n):
            res = 0
            while n > 0:
                res += pow(n%10, 2)
                n //= 10
            return res
        
        if n == 1: return True
        if n == 10: return True

        while (n != 1 or n != 7) and n > 9:
            if n == 1 or n == 7: return True
            n = sum_of_squares(n)
            
        if n == 1 or n == 7: return True
        
        return False