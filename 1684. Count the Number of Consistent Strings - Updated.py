class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            lst = []
            lst[:] = word
            flag = 1
            for i in range(len(lst)):
                if lst[i] not in allowed:
                    flag = 0
                    break
            if flag == 1:
                count += 1
        return count

