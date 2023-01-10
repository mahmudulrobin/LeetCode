class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        string = list(map(str, s))
        result = []
        increment = 0
        decrement = len(string) + 1
        flag = 0
        I_first_val_check = 0
        for i in range(len(string)):
            if string[i] == "I":
                if I_first_val_check == 0:
                    result.append(increment)

                else:
                    increment += 1
                    result.append(increment)
                flag = 0
                I_first_val_check = 1

            else:
                decrement -= 1
                result.append(decrement)
                flag = 1
        if flag == 1:
            decrement -= 1
            result.append(decrement)
            return result
        else:
            increment += 1
            result.append(increment)
            return result
