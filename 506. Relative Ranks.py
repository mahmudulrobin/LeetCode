class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dic={}
        for i in range(len(score)):
            dic[score[i]]=i
        score.sort(reverse=True)
        dic_rank={}
        #rank based on higher score
        for i in range(len(score)):
            dic_rank[score[i]]=str(i+1)
        #Mapping with rank
        for j in score:
            dic[j]=dic_rank[j]
        answer=[]
        for key, value in dic.items():
            if value=="1":
                answer.append("Gold Medal")
            elif value=="2":
                answer.append("Silver Medal")
            elif value=="3":
                answer.append("Bronze Medal")
            else:
                answer.append(value)
        return answer
