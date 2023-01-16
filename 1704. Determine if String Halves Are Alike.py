class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half=len(s)//2
        a=""
        b=""
        vowel=['a', 'e', 'i', 'o', 'u', 'A','E', 'I', 'O', 'U']
        for i in range(len(s)):
            if i<half:
                a+=s[i]
            else:
                b+=s[i]
        count_a=0
        count_b=0
        for i in range(half):
            if a[i] in vowel:
                count_a+=1
            if b[i] in vowel:
                count_b+=1
        if count_a==count_b:
            return True
        else:
            return False