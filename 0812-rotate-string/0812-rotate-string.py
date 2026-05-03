class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        def rotate_by_one(s):
            return s[1:] + s[0]
        
        if len(s) != len(goal): return False
        
        i = 0

        while i < len(s):
            s = rotate_by_one(s)
            print(s)
            if s == goal: return True
            i += 1
        
        return False