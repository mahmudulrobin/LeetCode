class Solution:
    def balancedStringSplit(self, s: str) -> int:
        s = str(s)
        res = []
        res[:] = s
        count_r = 0
        count_l = 0
        result = 0
        for i in range(len(res)):
            if res[i] == "R":
                count_r += 1
            if res[i] == "L":
                count_l += 1
            if count_r == count_l:
                result += 1
        return result


