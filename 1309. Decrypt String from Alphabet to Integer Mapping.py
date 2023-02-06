class Solution:
    def freqAlphabets(self, s: str) -> str:
        str=string.ascii_lowercase
        i=0
        res=""
        flag=0
        while i<=len(s)-3:
            cmp=""
            if s[i+2]=="#":
                cmp+=s[i]+s[i+1]
                res+=str[int(cmp)-1]
                i+=3
                if (len(s)-1)-i==2:
                    flag=1
                continue
            else:
                res+=str[int(s[i])-1]
                i+=1
        if flag==0:
            while (len(s)-1)-i>=0:
                res+=str[int(s[i])-1]
                i+=1
        return res