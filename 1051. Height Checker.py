class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_height = sorted(heights)
        result = 0
        for i in range(len(heights)):
            if heights[i] != sorted_height[i]:
                result += 1
        return result
