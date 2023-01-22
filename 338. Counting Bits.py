class Solution:
    def countBits(self, n: int) -> List[int]:
        output=[]
        for i in range(n+1):
            binary=bin(i)
            lst=list(binary)
            lst.remove("b")
            lst=list(map(int, lst))
            output.append(lst.count(1))
        return output
