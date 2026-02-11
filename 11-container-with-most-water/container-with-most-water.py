class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = -1
        while l < r:
            maxArea = max(min(height[l], height[r]) * (r - l), maxArea)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxArea

