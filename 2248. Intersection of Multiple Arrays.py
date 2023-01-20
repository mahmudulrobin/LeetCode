class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        result=[]
        cmp=[]
        for i in range(1,len(nums)):
            cmp.append(nums[i])
        if len(nums)>1:
            for i in range(len(nums[0])):
                c=0
                for j in range(len(cmp)):
                    if nums[0][i] in cmp[j]:
                        c+=1
                    if c==len(cmp):
                        result.append(nums[0][i])
                        break
            return sorted(result)
        else:
            return sorted(nums[0])