class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                prev_start, prev_height = stack.pop()
                width = i - prev_start
                maxArea = max(maxArea, prev_height * width)
                start = prev_start
            stack.append((start, height))
        n = len(heights)
        while stack:
            start, height = stack.pop()
            maxArea = max(maxArea, height * (n - start))
        return maxArea