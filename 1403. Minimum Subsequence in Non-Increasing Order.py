class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total = 0
        result = []
        seq_sum = 0
        for i in range(len(nums)):
            total += nums[i]
        for i in range(len(nums)):
            if seq_sum <= total:
                total -= nums[i]
                seq_sum += nums[i]
                result.append(nums[i])
        return result

