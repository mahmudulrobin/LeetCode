class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        position.sort()
        l=len(position)
        even=0
        odd=0
        for i in range(l):
            if position[i]%2==0:
                even+=1
            else:
                odd+=1
        if even!=l or odd!=l:
            return min(even,odd)
        else:
            return 0