class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        unique_list1=[]
        for i in range(len(words1)):
            count=words1.count(words1[i])
            if count==1:
                unique_list1.append(words1[i])
            count=0
        unique_list2=[]
        for i in range(len(words2)):
            count=words2.count(words2[i])
            if count==1:
                unique_list2.append(words2[i])
            count=0
        output=0
        for i in range(len(unique_list1)):
            if unique_list1[i] in unique_list2:
                output+=1
        return output