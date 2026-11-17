class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=[]
        for i in range(len(words)):
            count=0
            for j in range(len(words)):
                if words[i] in words[j]:
                    count+=1
                if count>1:
                    ans.append(words[i])
                    break
        

        return list(set(ans))

        