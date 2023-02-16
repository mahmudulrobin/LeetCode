class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        unique=list(set(groupSizes))
        result=[]
        for i in range(len(unique)):
            c=1
            flag=1
            arr=[]
            for j in range(len(groupSizes)):
                if unique[i]==groupSizes[j]:
                    if c<=unique[i]:
                        if flag==1:
                            result.append(arr)
                            arr=[]
                            flag=0
                        arr.append(j)
                        c+=1
                        if c>unique[i]:
                            c=1
                            flag=1
            result.append(arr)
        res = [ele for ele in result if ele != []]
        return res


