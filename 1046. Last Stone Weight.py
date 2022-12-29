class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        else:
            while len(stones)>1:
                stones.sort()
                last=stones[-1]
                last2=stones[-2]
                if len(stones)==2 and last==last2:
                    del stones[-1]
                    del stones[-1]
                    return 0
                else:
                    if last==last2:
                        del stones[-1]
                        del stones[-1]
                    else:
                        stones[-1]=last-last2
                        del stones[-2]
        return stones[0]