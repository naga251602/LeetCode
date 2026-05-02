class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for word in strs:
            c = [0] * 26
            for char in word:
                c[ord(char) - 97] += 1
            key = tuple(c)
            hm[key].append(word)
        
        return list(hm.values())