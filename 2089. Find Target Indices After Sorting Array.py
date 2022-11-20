class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result=[]
        for j in range(len(nums)):
            if nums[j]>target:
                break
            if nums[j]==target:
                result.append(j)
        return result