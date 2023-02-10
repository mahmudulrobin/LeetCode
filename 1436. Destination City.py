class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = []
        destination = []
        for i, j in paths:
            start.append(i)
            destination.append(j)
        for dest in destination:
            if dest not in start:
                return dest


