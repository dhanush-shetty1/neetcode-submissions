class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=0

        left=0
        right=0

        while right<len(nums):
            if nums[right]==0:
                right+=1
                left=right
            else:
                ans=max(ans,right-left+1)
                right+=1
        
        return ans

        