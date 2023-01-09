class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                cal = (nums[i] + 1) - nums[i + 1]
                nums[i + 1] += cal
                res += cal
        return res

