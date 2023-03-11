class Solution:
    def countDigits(self, num: int) -> int:
        digits = list(map(int, str(num)))
        result=0
        for i in digits:
            if num%i==0:
                result+=1
        return result
