class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort(reverse=True)
        time=0
        while any(cups>0 for cups in amount):
            if amount[0]>0:
                amount[0]-=1
            if amount[1]>0:
                amount[1]-=1
            time+=1
            amount.sort(reverse=True)
        return time
