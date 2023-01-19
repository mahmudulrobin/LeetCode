class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        substring=[]
        string=""
        for i in range(len(s)-2):
            string=""
            for j in range(i,i+3,1):
                string+=s[j]
            substring.append(string)
        result=[]
        count=0
        for i in range(len(substring)):
            unique=set(substring[i])
            result.append(list(unique))
            if len(substring[i])==len(result[i]):
                count+=1
        return count
