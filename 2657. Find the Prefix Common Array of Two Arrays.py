class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        list1 = []
        list2 = []
        count = 0
        output = []
        for i in range(len(A)):
            list1.append(A[i])
            list2.append(B[i])
            count = len([w for w in list2 if w in list1])
            output.append(count)
        return output
