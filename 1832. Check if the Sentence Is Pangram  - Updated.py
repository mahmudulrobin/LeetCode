class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        lst = []
        lst = list(map(chr, range(ord('a'), ord('z') + 1)))
        for i in sentence:
            if i in lst:
                lst.remove(i)
        if lst:
            return False
        else:
            return True

