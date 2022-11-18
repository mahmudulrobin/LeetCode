class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        x = 0
        result = []
        while x < 2:
            for i in range(len(nums)):
                if i < len(nums) - 1:
                    if nums[i] > nums[i + 1]:
                        nums[i + 1], nums[i] = nums[i], nums[i + 1]
            result.append(nums[-1])
            if x == 0:
                nums.pop(len(nums) - 1)
            x += 1
        y = 0
        while y < 2:
            for i in range(len(nums)):
                if i < len(nums) - 1:
                    if nums[i] < nums[i + 1]:
                        nums[i + 1], nums[i] = nums[i], nums[i + 1]
            result.append(nums[-1])
            if y == 0:
                nums.pop(len(nums) - 1)
            y += 1
        return (result[0] * result[1] - result[2] * result[3])


