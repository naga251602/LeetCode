class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        for i in range(len(digits) - 1, -1, -1):
            val = digits[i] + c
            digits[i] = (val%10)
            c = val // 10
        if c != 0: return [c] + digits
        return digits