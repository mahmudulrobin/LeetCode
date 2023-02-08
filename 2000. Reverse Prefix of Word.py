class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        else:
            ind = word.index(ch)
            res = ""
            flag = 0
            for i in range(len(word) - 1, -1, -1):
                if i <= ind:
                    res += word[i]
            for i in range(ind + 1, len(word)):
                res += word[i]
            return res
