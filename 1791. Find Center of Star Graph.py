class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        for i in range(len(edges)):
            for j in edges[i]:
                count = 0
                for k in range(len(edges) - 1):
                    if j == edges[k + 1][0] or j == edges[k + 1][1]:
                        count += 1
                if count == len(edges) - 1:
                    return j

