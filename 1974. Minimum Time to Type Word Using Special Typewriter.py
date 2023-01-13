class Solution:
    def minTimeToType(self, word: str) -> int:
        alphabets=list(map(chr, range(ord('a'), ord('z')+1)))
        dic={}
        for i in range(len(alphabets)):
            dic[alphabets[i]]=i+1
        words=[*word]
        time=0
        max=26
        min=1
        for i in range(len(words)):
            if i==0:
                if dic[words[i]]<=13:
                    if dic[words[i]]!=1:
                        time+=dic[words[i]]-min+1
                    else:
                        time+=1
                else:
                    time+=(max-dic[words[i]])+2
            else:
                if dic[words[i]]-dic[words[i-1]]<0 and dic[words[i]]-dic[words[i-1]]<-13:
                    time+=dic[words[i]]+(max-dic[words[i-1]])+1
                elif dic[words[i]]-dic[words[i-1]]<0 and dic[words[i]]-dic[words[i-1]]>=-13:
                    time+=dic[words[i-1]]-dic[words[i]]+1
                elif dic[words[i]]-dic[words[i-1]]>0 and dic[words[i]]-dic[words[i-1]]<13:
                    time+=dic[words[i]]-dic[words[i-1]]+1
                elif dic[words[i]]-dic[words[i-1]]>0 and dic[words[i]]-dic[words[i-1]]>=13:
                    time+=dic[words[i-1]]+ (max-dic[words[i]])+1
                elif dic[words[i]]-dic[words[i-1]]==0:
                    time+=1
        return time