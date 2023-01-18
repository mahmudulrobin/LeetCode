class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        l = len(nums)
        nums.sort()
        flag = 0
        for i in range(0, l - 1, 2):
            if nums[i] != nums[i + 1]:
                flag = 1
                break
        if flag == 1:
            return False
        else:
            return True

