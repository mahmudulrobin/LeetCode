class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        for x_circle, y_circle, r in queries:
            count = 0
            for x, y in points:
                if ((x - x_circle) ** 2 + (y - y_circle) ** 2) <= r ** 2:
                    count += 1
            result.append(count)
        return result