class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        cmp=[]
        for i in score:
            cmp.append(i[k])
        cmp.sort(reverse=True)
        for i in cmp:
            for j in score:
                if i==j[k]:
                    res.append(j)
                    break
        return res

