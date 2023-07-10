class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        lst = []
        lst = list(map(chr, range(ord('a'), ord('z') + 1)))
        mapp = {}
        for i in range(len(lst)):
            mapp[lst[i]] = morse_code[i]
        ans = []
        for word in words:
            result = ""
            List = []
            List[:] = word
            for letter in List:
                result += mapp[letter]
            ans.append(result)
        return len(set(ans))


