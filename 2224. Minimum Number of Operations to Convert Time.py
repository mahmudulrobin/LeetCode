class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        cur_list = [*current]
        cur_list.pop(2)
        a = int(str(cur_list[0]) + str(cur_list[1]))
        a = a * 60
        b = int(str(cur_list[2]) + str(cur_list[3]))
        curr = a + b
        cor_list = [*correct]
        cor_list.pop(2)
        x = int(str(cor_list[0]) + str(cor_list[1]))
        x = x * 60
        y = int(str(cor_list[2]) + str(cor_list[3]))
        corr = x + y

        operation = 0
        lst = [60, 15, 5, 1]
        result = []
        flag = 0

        if corr - curr != 0:
            sub = abs(corr - curr)
            if sub >= lst[0]:
                calc = sub // lst[0]
                operation += calc
                sub -= calc * lst[0]
            if sub >= lst[1]:
                calc = sub // lst[1]
                operation += calc
                sub -= calc * lst[1]
            if sub >= lst[2]:
                calc = sub // lst[2]
                operation += calc
                sub -= calc * (lst[2])
            if sub >= lst[3]:
                calc = sub // lst[3]
                operation += calc
                sub -= calc * lst[3]
        else:
            flag = 1
            return 0
        if flag == 0:
            return operation


