class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        result = 0
        l = len(cost)
        count = 0
        if l <= 2:
            if l == 1:
                result = cost[0]
            else:
                result = cost[0] + cost[1]
        else:
            for i in range(l):
                count += 1
                if i >= 2:
                    if count % 3 == 0:
                        pass
                    else:
                        result += cost[i]
                else:
                    result += cost[i]
        return result

