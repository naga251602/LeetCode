class Solution:
    def isValid(self, s: str) -> bool:
        st = list()

        for i in s:
            if len(st) > 0 and((st[-1] == '(' and i == ')') or (st[-1] == '[' and i == ']') or (st[-1] == '{' and i == '}')):
                st.pop()
            else:
                st.append(i)
        
        return len(st) == 0
            