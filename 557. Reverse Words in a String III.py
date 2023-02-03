class Solution:
    def reverseWords(self, s: str) -> str:
        string=""
        s=s.split()
        rev=[]
        for i in s:
            rev.append(i[::-1])
        return " ".join(rev)