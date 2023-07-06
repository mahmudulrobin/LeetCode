class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        lst =[]
        lst = s.split(" ")
        final=""
        for i in range(k):
            if i<k-1:
                final+=lst[i]+" "
            else:
                final+=lst[i]
        return final
