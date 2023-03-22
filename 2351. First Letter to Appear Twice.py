class Solution:
    def repeatedCharacter(self, s: str) -> str:
        setCheck= set()
        for i in range(len(s)):
            if s[i] in setCheck:
                return s[i]
            else:
                setCheck.add(s[i])
