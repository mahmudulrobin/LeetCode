class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        out=""
        count=0
        for i in s:
            if i==" ":
                count+=1
                if count==k:
                    break
                out+=i
                continue
            out+=i
        return out
