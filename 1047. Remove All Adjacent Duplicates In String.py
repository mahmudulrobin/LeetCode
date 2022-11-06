class Solution:
    def removeDuplicates(self, s: str) -> str:
        result=[]
        l=len(s)
        for i in range(l):
            if i>=1:
                if result and result[-1]==s[i]:
                    result.pop()
                else:
                    result.append(s[i])
            else:
                result.append(s[i])
        return "".join(result)