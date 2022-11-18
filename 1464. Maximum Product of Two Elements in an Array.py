class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        result = []
        for i in range(l):
            for j in range(i + 1, l):
                mul = (nums[i] - 1) * (nums[j] - 1)
                result.append(mul)
                if len(result) > 1:
                    if result[0] > result[1]:
                        result.pop(1)
                    else:
                        result.pop(0)
        res = "".join(map(str, result))
        return int(res)
