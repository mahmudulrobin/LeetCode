class Solution:
    def tribonacci(self, n: int) -> int:
        first=0
        second=1
        next=1
        if n<=2:
            if n==0:
                return first
            else:
                return second
        for i in range(3,n+1):
            temp_second=second
            temp_next=next
            next+=first+second
            second=temp_next
            first=temp_second
        return next
