class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        for i in range(len(digits) - 1, -1, -1):
            tot = digits[i] + c
            c = tot //10
            digits[i] = tot%10

            
        if c != 0:
            digits.insert(0, c)

        return digits
        