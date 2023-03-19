class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        fact=0
        for i in range(1,b+1):
            if b%i==0 and a%i==0:
                fact+=1
        return fact
