class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            if ord(s[i]) >= 65 and ord(s[i]) <= 90:
                result += chr(ord(s[i]) + 32)
                continue
            result += s[i]
        return result
