class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost)-2,-1,-1):
            if i==len(cost)-2:
                cost[i]=cost[i]+cost[i+1]
            else:
                cost[i]= min((cost[i]+cost[i+1]),(cost[i]+cost[i+2]))
        return min(cost[0],cost[1])