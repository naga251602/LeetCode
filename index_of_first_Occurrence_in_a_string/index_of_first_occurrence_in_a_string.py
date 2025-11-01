class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) == 1:
            for i in range(len(haystack)):
                if haystack[i] == needle[0]: return i
        
        st, en = 0, len(needle) 

        while  en <= len(haystack):
            if haystack[st:en] == needle: return st
            else:
                st += 1
                en += 1
        
        return -1