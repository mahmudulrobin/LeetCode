class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        calc=[[1]]
        for i in range(1,rowIndex+1):
            temp=[0]+calc[-1]+[0]
            row=[]
            for j in range(len(calc[-1])+1):
                row.append(temp[j]+temp[j+1])
            calc.append(row)
        return calc[-1]

