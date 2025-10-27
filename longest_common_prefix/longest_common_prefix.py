class Solution:
    @staticmethod
    def check_prefix(word_1, word_2):

        i, j = 0, 0
        res = ""

        while i < len(word_1) and j < len(word_2):
            if word_1[i] == word_2[j]:
                res += word_1[i]
                i += 1
                j += 1
            else:
                
                return res if i != 0 else ""
        return res
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        
        res = strs[0]
        
        # effective time complexity O(n ^ m)
        # n = no of word in the list
        # m = length of word_1
        for i in range(1, len(strs)):
            res = self.check_prefix(res, strs[i])

        return res

        

