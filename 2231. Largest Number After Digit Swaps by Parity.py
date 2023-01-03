class Solution:
    def largestInteger(self, num: int) -> int:
        lst = list(map(int, str(num)))
        lst.sort(reverse=False)
        l = len(lst)
        result = []
        even = []
        odd = []
        for i in range(len(lst)):
            if lst[i] % 2 == 0:
                even.append(lst[i])
            else:
                odd.append(lst[i])
        even.sort(reverse=True)
        odd.sort(reverse=True)

        num = str(num)
        print(num, lst)

        ans = []
        o = len(odd)
        e = len(even)
        k = 0
        i = 0
        j = 0
        while k < l:
            if int(num[k]) % 2 == 0:
                ans.append(even[i])
                i += 1
            else:
                ans.append(odd[j])
                j += 1
            k += 1
        answer = [str(i) for i in ans]
        res = int(''.join(answer))
        return res


