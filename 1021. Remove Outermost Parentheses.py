class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        stack = []
        for i in s:
            if i == "(":
                count += 1
                if count != 1:
                    stack.append(i)
            elif i == ")":
                count -= 1
                if count != 0:
                    stack.append(i)
        return "".join(stack)

