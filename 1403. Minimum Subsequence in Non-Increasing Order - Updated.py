class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums=sorted(nums, reverse=True)
        res=[]
        if len(nums)==1:
            res.append(nums[0])
            return res
        else:
            for i in range(len(nums)):
                if sum(nums[0:i+1])>sum(nums[i+1:]):
                    for k in range(i+1):
                        res.append(nums[k])
                    return res


