class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False

        res = []

        for i in range(len(s)):
            if len(res) > 0 and ((res[len(res) - 1] == '(' and s[i] == ')') or (res[len(res) - 1] == '{' and s[i] == '}') or (res[len(res) - 1] == '[' and s[i] == ']')):
                res.pop()
            else:
                res.append(s[i])

        return len(res) == 0

            