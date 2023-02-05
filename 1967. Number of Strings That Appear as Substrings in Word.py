class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        c=0
        for i in range(len(patterns)):
            if patterns[i] in word:
                c+=1
        return c
