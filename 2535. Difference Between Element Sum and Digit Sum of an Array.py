class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum=0
        ind_sum=0
        for i in nums:
            sum+=i
            s=str(i)
            for j in s:
                ind_sum+=int(j)
        return abs(sum-ind_sum)
