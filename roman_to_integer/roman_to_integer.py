class Solution:
    def romanToInt(self, s: str) -> int:
        data = {
               'I':1, 
                'V':5,
                'X':10,
                'L':50,
                'C': 100,
                'D': 500,
                'M': 1000
        }

        total = 0

        for i in range(0, len(s)):
            if i != 0 and data[s[i-1]] < data[s[i]]:
                total = total + data[s[i]] - 2 * data[s[i - 1]]
            else: total += data[s[i]]

        return total