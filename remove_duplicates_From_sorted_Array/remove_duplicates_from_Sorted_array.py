class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        pos = 0

        for i in range(1, len(arr)):
            if arr[pos] != arr[i]:
                pos += 1
                arr[pos], arr[i] = arr[i], arr[pos]
        
        return pos+1