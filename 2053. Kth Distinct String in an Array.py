class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = 0
        unique_list = []
        for i in range(len(arr)):
            count = arr.count(arr[i])
            if count == 1:
                unique_list.append(arr[i])
            count = 0
        result = ""
        flag = 0
        if len(unique_list) == 0:
            return ""
        else:
            for i in range(0, len(unique_list)):
                if i == k - 1:
                    result += unique_list[i]
                    flag = 1
                    break
        if flag == 0:
            return ""
        else:
            return result

