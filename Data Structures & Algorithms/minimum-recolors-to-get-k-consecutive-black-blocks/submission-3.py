from collections import defaultdict
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count=0
        ans=float("INF")
        left=0
        c=defaultdict(int)

        for ch in blocks:
            c[ch]+=1
        if len(blocks)==k:
            return c["W"]

        for right in range(len(blocks)-k):
            temp=blocks[right:right+k]

            while left<right+k:
                if blocks[left]=="W":
                    count+=1
                left+=1
            ans=min(ans,count)
            count=0
            left=right+1
        
        return ans
        


        
        