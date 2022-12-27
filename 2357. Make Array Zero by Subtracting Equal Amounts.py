class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l = len(nums)
        count = 0
        while len(nums) > 0:
            nums.sort()
            while len(nums) > 0 and nums[0] == 0:
                nums.pop(0)
            if len(nums) > 0:
                sub = nums[0]
                for i in range(len(nums)):
                    nums[i] -= sub
                count += 1
        return count

