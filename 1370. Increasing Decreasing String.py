class Solution:
    def sortString(self, s: str) -> str:
        alphabet = list(string.ascii_lowercase)
        dic = {}
        for i in range(len(alphabet)):
            dic[i] = alphabet[i]
        lst = []
        for i in range(len(s)):
            num = ord(s[i]) - 97
            lst.append(num)
        result = []

        while lst:
            unique = set(lst)
            unique_list = list(unique)
            while unique_list:
                step1 = min(unique_list)
                result.append(step1)
                unique_list.remove(step1)
                lst.remove(step1)
            if lst:
                unique = set(lst)
                unique_list = list(unique)
                while unique_list:
                    step2 = max(unique_list)
                    result.append(step2)
                    unique_list.remove(step2)
                    lst.remove(step2)
        ans = ""
        for i in range(len(result)):
            ans += dic[result[i]]
        return ans











