from collections import defaultdict
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count=0
        for i in range(k):
            if blocks[i]=="W":
                count+=1
        ans=count
        for right in range(k,len(blocks)):
            if blocks[right]=="W":
                count+=1
            if blocks[right-k]=="W":
                count-=1
            ans=min(count,ans)
        
        return ans
        


        
        