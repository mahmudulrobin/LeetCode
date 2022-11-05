class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l = len(operations)
        result = []
        result_sum = 0
        for i in range(l):
            if operations[i] == "+":
                result.append(int(result[-1]) + int(result[-2]))
            elif operations[i] == "D":
                result.append(int(result[-1]) * 2)
            elif operations[i] == "C":
                del result[-1]
            else:
                result.append(int(operations[i]))
        for j in result:
            result_sum += int(j)
        return result_sum








