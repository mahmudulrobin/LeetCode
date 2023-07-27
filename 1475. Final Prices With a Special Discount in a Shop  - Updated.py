class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        for i in range(len(prices)):
            new_price = prices[i]
            flag = 0
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    new_price -= prices[j]
                    result.append(new_price)
                    flag = 1
                    break
            if flag == 0:
                result.append(new_price)
        return result


