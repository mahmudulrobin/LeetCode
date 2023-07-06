class Solution:
    def sortSentence(self, s: str) -> str:
        lst = []
        lst = s.split(" ")
        dic = {}
        n = []
        for i in lst:
            num = int(i[-1])
            n.append(num)
            i = i.replace(i[-1], "")
            dic[num] = i
        n = sorted(n)
        final = ""
        for i in range(len(n)):
            if i < len(n) - 1:
                final += dic[n[i]] + " "
            else:
                final += dic[n[i]]
        return final


