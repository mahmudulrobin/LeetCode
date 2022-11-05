class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        l = len(prices)
        result = []
        for i in range(l):
            flag = 0
            for j in range(i + 1, l):
                if prices[j] <= prices[i]:
                    flag = 1
                    result.append(prices[i] - prices[j])
                    break
            if flag == 0:
                result.append(prices[i])
        return result

