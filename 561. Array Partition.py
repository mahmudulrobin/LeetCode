class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        pair = []
        sum = 0
        result = []
        for i in range(0, l, 2):
            pair.append(nums[i])
            pair.append(nums[i + 1])
            result.append(min(pair))
            pair = []
        for i in result:
            sum += i
        return sum
