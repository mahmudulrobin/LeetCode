class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        result = []
        exist = []
        for i in range(len(nums)):
            flag = 0
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    flag = 1
                    exist.append(nums[j])
                    break
            if flag == 0:
                if nums[i] not in exist:
                    result.append(nums[i])
        output = 0
        for i in range(len(result)):
            output += result[i]
        return output



