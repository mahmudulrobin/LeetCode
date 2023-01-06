class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums_sort=sorted(nums,reverse=True)
        nums_sorted=[]
        nums_sorted=[nums_sort[i] for i in range(k)]
        result=[]
        for i in range(len(nums)):
            for j in range(len(nums_sorted)):
                if nums[i]==nums_sorted[j]:
                    result.append(i)
                    nums_sorted.remove(nums[i])
                    break
        ans=[]
        for i in result:
            ans.append(nums[i])
        return ans


