class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count_p=0
        count_n=0
        for i in range(len(nums)):
            if nums[i]<0:
                count_n+=1
            elif nums[i]>0:
                count_p+=1
        if count_p>count_n:
            return count_p
        else:
            return count_n