class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result = []
        odd = []
        for i in nums:
            if i % 2 == 0:
                result.append(i)
            else:
                odd.append(i)
        result.extend(odd)
        return result
