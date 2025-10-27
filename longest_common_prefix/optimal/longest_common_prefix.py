class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        
        res = ""

        strs.sort()

        for i in range(min(len(strs[0]), len(strs[len(strs) - 1]))):
            if strs[0][i] != strs[len(strs) - 1][i] : return res
            else:
                res += strs[0][i]

        return res