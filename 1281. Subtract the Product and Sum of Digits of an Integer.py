class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = list(map(int, str(n)))
        mul=1
        sum=0
        for val in digits:
            mul*=val
            sum+=val
        return mul-sum

