class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pair=0
        unique=set(nums)
        unique_list=list(unique)
        c=0
        leftover=0
        for i in range(len(unique_list)):
            c=nums.count(unique_list[i])
            pair+=c//2
            if c%2!=0:
                leftover+=c%2
        return [pair,leftover]