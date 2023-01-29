class Solution:
    def interpret(self, command: str) -> str:
        res=[]
        l=len(command)
        for i in range(l):
            if command[i]=="G":
                res.append("G")
            elif command[i]=="(":
                if command[i+1]==")":
                    res.append("o")
                    continue
                elif command[i+1]=="a" and command[i+2]=="l":
                    res.append("al")
                    continue
        return "".join(res)
