class Solution:
    def divisorGame(self, n: int) -> bool:
        count = 0
        x = 1
        while n != 1:
            if x > 0 and x < n and n % x == 0:
                count += 1
                n -= x
        if count % 2 == 0:
            return False
        else:
            return True
