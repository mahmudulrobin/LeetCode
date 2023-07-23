class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums=sorted(nums)
        count=0
        for i in range(len(nums)):
            if nums[i]!=0:
                minimum=nums[i]
                for j in range(i,len(nums)):
                    nums[j]-=minimum
                count+=1
        return count


