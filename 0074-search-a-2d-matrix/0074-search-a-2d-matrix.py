class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                st, en = 0, len(matrix[i]) - 1
                while st <= en:
                    m = st + (en - st) // 2
                    if matrix[i][m] == target: return True
                    elif matrix[i][m] < target: st = m + 1
                    else: en = m - 1
            else: continue
        
        return False
