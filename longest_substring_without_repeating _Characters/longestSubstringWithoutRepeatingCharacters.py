class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1: return len(s)

        i, j = 0, 1
        max_len = 1
        
        while i < len(s) and j < len(s):
            if s[j] not in s[i: j]:
                j += 1
            else:
                i += 1
            max_len = max([max_len, len(s[i: j])])
        
        return max_len