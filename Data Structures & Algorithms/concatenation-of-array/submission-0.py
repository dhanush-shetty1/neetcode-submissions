class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        L=[1]*n
        for i in range(len(nums)):
            L[i]=nums[i]
        
        nums.extend(L)
        return nums

        