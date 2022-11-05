class Solution:
    def maxDepth(self, s: str) -> int:
        max_count = 0
        count = 0
        stack = []
        for letter in s:
            if letter == "(":
                count += 1
                stack.append(letter)
                if count > max_count:
                    max_count = count
            if letter == ")":
                stack.pop()
                count -= 1
        return max_count
