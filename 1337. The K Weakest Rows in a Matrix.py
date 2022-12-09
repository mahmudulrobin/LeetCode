class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dic={}
        for ele in range(len(mat)):
            soldier_count=0
            for num in range(len(mat[ele])):
                if mat[ele][num]==1:
                    soldier_count+=1
            dic[ele]=soldier_count
        sorted_dic = dict( sorted(dic.items(), key=operator.itemgetter(1),reverse=False))
        key_list = list(sorted_dic.keys())
        result=[]
        for i in range(k):
            result.append(key_list[i])
        return result
