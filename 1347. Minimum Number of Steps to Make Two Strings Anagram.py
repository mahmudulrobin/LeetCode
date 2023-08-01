class Solution:
    def minSteps(self, s: str, t: str) -> int:
        for i in s:
            t= t.replace(i, "", 1)
        return len(t)


