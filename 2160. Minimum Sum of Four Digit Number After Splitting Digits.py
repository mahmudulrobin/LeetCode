class Solution:
    def minimumSum(self, num: int) -> int:
        pair1 = []
        pair2 = []
        lst = []
        for i in str(num):
            lst.append(i)
        lst.sort()
        for i in range(len(lst)):
            if i % 2 == 0:
                pair1.append(lst[i])
            else:
                pair2.append(lst[i])
        pair1_string = "".join(pair1)
        pair2_string = "".join(pair2)
        print(pair1_string, pair2_string)
        min_sum = int(pair1_string) + int(pair2_string)
        return min_sum

