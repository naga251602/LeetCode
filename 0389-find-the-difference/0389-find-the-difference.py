class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0: return t
        h = [0] * 26
        
        for i in range(len(s)):
            h[ord(s[i]) - 97] += 1
            h[ord(t[i]) - 97] -= 1
        h[ord(t[i+1]) - 97] -= 1
        
        for i in range(0, 26):
            if h[i] == -1: break
        
        return chr(97 + i)