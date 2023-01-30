class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        inp=[]
        for i in range(len(s)):
            if s[i]==":":
                continue
            inp.append(s[i])
        res=""
        inp_str=""
        inp_int=""
        inp_str=inp[0]+inp[2]
        inp_int=inp[1]+inp[3]
        range_chr=abs(ord(inp_str[0])-ord(inp_str[1]))
        range_int=abs(int(inp_int[0])-int(inp_int[1]))
        output=[]
        for i in range(range_chr+1):
            res+=chr(ord(inp_str[0])+i)
            for j in range(range_int+1):
                val=int(inp_int[0])+j
                res+=str(val)
                output.append(res)
                res=res.replace(str(val),"")
            res=""
        return output