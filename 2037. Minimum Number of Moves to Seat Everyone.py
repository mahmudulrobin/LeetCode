class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        l_std=len(students)
        seats.sort()
        students.sort()
        count=0
        for i in range(l_std):
            if students[i]!=seats[i]:
                val=abs(students[i]-seats[i])
                count+=val
        return count

