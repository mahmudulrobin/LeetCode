class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        temp=[]
        for i in range(n+1):
            if i==0:
                temp.append(0)
            elif i==1:
                temp.append(1)
            elif i%2==0:
                temp.append(temp[i//2])
            else:
                temp.append(temp[i//2]+temp[i//2+1])
        return max(temp)