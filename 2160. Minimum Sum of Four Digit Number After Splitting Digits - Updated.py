class Solution:
    def minimumSum(self, num: int) -> int:
        lst = []
        num = str(num)
        lst = list(map(int, num))
        lst = sorted(lst)
        first_num = str(lst[0]) + str(lst[-1])
        second_num = str(lst[1]) + str(lst[-2])
        return int(first_num) + int(second_num)



