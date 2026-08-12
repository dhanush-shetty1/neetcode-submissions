class Solution:  
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans=[]
        left=1

        while left<len(arr):
            temp=arr[left:]
            m=max(temp)
            ans.append(m)
            left+=1
        
        ans.append(-1)

        return ans



            
        