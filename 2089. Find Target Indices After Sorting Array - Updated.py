class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums=sorted(nums)
        result=[]
        for i in range(len(nums)):
            if target==nums[i]:
                result.append(i)
        return result
