class Solution:
    def largestOddNumber(self, num: str) -> str:
        index=-1
        for i in range(len(num)):
            if int(num[i])%2!=0:
                index=i
        if index==-1:
            return ""
        else:
            return num[:index+1]


