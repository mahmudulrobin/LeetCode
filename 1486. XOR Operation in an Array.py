class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        xor = 0
        for i in range(n):
            calc = start + 2 * i
            nums.append(calc)
        for i in nums:
            xor = xor ^ i
        return xor

