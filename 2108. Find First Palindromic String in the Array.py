class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            l = len(words[i])
            for j in range(l):
                if words[i][j] != words[i][l - 1 - j]:
                    break
                elif j == l - 1:
                    return words[i]
        return ""


