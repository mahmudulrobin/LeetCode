class Solution:
    def maximum69Number (self, num: int) -> int:
        new_num=list(map(int, str(num)))
        for i in range(len(new_num)):
            if new_num[i]!=9:
                new_num[i]=9
                break
        res=""
        for i in range(len(new_num)):
            res+=str(new_num[i])
        return int(res)