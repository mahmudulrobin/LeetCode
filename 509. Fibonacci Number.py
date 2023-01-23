class Solution:
    def fib(self, n: int) -> int:
        first=0
        next=1
        if n<=1:
            if n==0:
                return first
            else:
                return next
        else:
            for i in range(2,n+1):
                temp=next
                next=next+first
                first=temp
            return next


