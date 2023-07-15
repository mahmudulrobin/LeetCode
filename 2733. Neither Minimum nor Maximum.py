class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]>min(nums) and nums[i]<max(nums):
                return nums[i]
        return -1