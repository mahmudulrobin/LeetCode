class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        sum=0
        left_sum=[0]
        for i in range(len(nums)-1):
            sum+=nums[i]
            left_sum.append(sum)
        s=0
        right_sum=[0]
        for j in range(len(nums)-1,0,-1):
            s+=nums[j]
            right_sum.append(s)
        right_sum.sort(reverse=True)
        res=[]
        for i in range(len(right_sum)):
            calc= abs(right_sum[i]-left_sum[i])
            res.append(calc)
        return res
