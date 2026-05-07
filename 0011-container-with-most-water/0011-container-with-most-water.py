class Solution:
    def maxArea(self, height: List[int]) -> int:
        st, en = 0, len(height) - 1
        max_water = 0

        while st < en:
            max_water = max(max_water, min(height[st], height[en]) * (en - st))
            if height[st] <= height[en]:
                st += 1
            else:
                en -= 1
        
        return max_water