class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic={}
        lst=[]
        for i in range(len(names)):
            dic[heights[i]]=names[i]
        heights=sorted(heights)
        for j in range(len(names)-1,-1,-1):
            lst.append(dic[heights[j]])
        return lst
