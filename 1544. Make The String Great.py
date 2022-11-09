class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        l = len(s)
        for i in range(l):
            if stack:
                if (stack[-1].isupper() and stack[-1].lower() == s[i]) or (
                        s[i].isupper() and s[i].lower() == stack[-1]):
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        return "".join(stack)
