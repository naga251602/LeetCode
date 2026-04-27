class Solution:
    def myAtoi(self, s: str) -> int:  
        s = s.strip()
        if len(s) == 0: return 0
        sign = -1 if s[0] == '-' else 1
        pl, nl = (2 ** 31) - 1, (2 ** 31)
        res = 0

        for i in range(len(s)):
            if i == 0 and (s[i] == '-' or s[i] == '+'): continue
            elif s[i].isdigit(): res = res * 10 + int(s[i])
            else: break

            if sign == 1 and res > pl : return pl
            elif sign == -1 and res > nl: return nl * sign
        
        return res * sign