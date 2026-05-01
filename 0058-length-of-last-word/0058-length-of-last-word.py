class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st = -1
        l = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ' ' and st == -1: continue
            elif s[i].isalpha() and (st == -1 or st == 1):
                l += 1
                st = 1
            else:
                break
            
        return l
            
        