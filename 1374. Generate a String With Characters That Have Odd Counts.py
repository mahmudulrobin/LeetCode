class Solution:
    def generateTheString(self, n: int) -> str:
        alphabet=string.ascii_lowercase
        res=""
        if n%2!=0:
            for i in range(1,n+1):
                res+=alphabet[0]
        else:
            for i in range(n):
                if i==n-1:
                    res+=alphabet[1]
                    break
                res+=alphabet[0]
        return res