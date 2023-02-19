class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            grid[i].sort(reverse=True)
        ans = 0
        for i in range(len(grid[0])):
            maxVal = 0
            for j in range(len(grid)):
                if grid[j][i] > maxVal:
                    maxVal = grid[j][i]
            ans += maxVal
        return ans

