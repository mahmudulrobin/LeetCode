class Solution:
    def digitCount(self, num: str) -> bool:
        c=0
        flag=0
        num=list(map(int, str(num)))
        for i in range(len(num)):
            c=num.count(i)
            if c!=num[i]:
                flag=1
                break
        if flag==1:
            return False
        else:
            return True
