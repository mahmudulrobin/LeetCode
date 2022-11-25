class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dic={}
        i1_len=len(items1)
        i2_len=len(items2)
        items1 = sorted(items1, key=lambda items1:items1[0])
        items2 = sorted(items2, key=lambda items2:items2[0])
        result1=[]
        result2=[]
        for i in range(i1_len):
            for j in range(i2_len):
                flag=0
                if items2[j][0]> items1[i][0]:
                    break
                elif items1[i][0]==items2[j][0]:
                    dic[items1[i][0]]=items1[i][1]+items2[j][1]
                    flag=1
                    break

            if flag==0:
                dic[items1[i][0]]=items1[i][1]

        #storing all the sum of the items1 value's weight
        for i in range(i1_len):
            result1.append([items1[i][0],dic[items1[i][0]]])
        result1 = sorted(result1, key=lambda result1:result1[0])
        result=result1

        #storing the rest of the uncommon items2's value & weight
        for i in range(i2_len):
            flag=0
            for j in range(len(result1)):
                if items2[i][0]!= result1[j][0]:
                    flag=0
                else:
                    flag=1
                    break
            if flag==0:
                result.append([items2[i][0], items2[i][1]])

        result = sorted(result, key=lambda result:result[0])
        return result
