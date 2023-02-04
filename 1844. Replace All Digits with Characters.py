class Solution:
    def replaceDigits(self, s: str) -> str:
        alphabet = list(string.ascii_lowercase)
        res=""
        dic={}
        for i in range(len(alphabet)):
            dic[alphabet[i]]=i
        s=list(s)
        for i in range(1,len(s),2):
                s[i]=alphabet[dic[s[i-1]]+int(s[i])]
        return "".join(s)
