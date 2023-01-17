class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        unique=set(s)
        unique_list=list(unique)
        count=0
        result=[]
        for i in range(len(unique_list)):
            count=0
            for j in range(len(s)):
                if unique_list[i]==s[j]:
                    count+=1
            result.append(count)
        if len(set(result))==1:
            return True
        else:
            return False

