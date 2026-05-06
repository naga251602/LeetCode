class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n == k or k%n == 0: return

        def rev(arr, st, en):
            while st < en:
                arr[st], arr[en] = arr[en], arr[st]
                st += 1
                en -= 1

        k = k%n
        rev(nums, 0, n - k - 1)
        rev(nums, n - k, n - 1)
        rev(nums, 0, n-1)