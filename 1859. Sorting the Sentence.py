class Solution:
    def sortSentence(self, s: str) -> str:
        l = len(s)
        dic = {}
        string = ""
        num_store = []
        for i in range(l):
            flag = 0
            if s[i].isnumeric() == True:
                dic[s[i]] = string.strip()
                flag = 1
                num_store.append(s[i])
                string = ""
            if flag == 0:
                string += s[i]
        res = ""
        num_store.sort()
        flag = 0
        for i in num_store:
            # if i==len(num_store):
            if i == num_store[-1]:
                res += dic[i]
                flag = 1
            if flag == 0:
                res += dic[i] + " "
        return res

