class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        L=nums[:]
        nums.extend(L)
        return nums
        

        