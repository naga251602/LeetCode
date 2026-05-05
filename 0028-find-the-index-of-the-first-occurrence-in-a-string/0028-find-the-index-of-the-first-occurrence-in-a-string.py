class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        for i in range(m-n+1):
            pos = 0
            
            while pos < n:
                if haystack[i+pos] != needle[pos]: break
                pos += 1
            
            if pos == n: return i

        return -1