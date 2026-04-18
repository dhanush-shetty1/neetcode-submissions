class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L=[]
        for i in range(len(nums)):
            prod=1
            for j in range(len(nums)):
                if i!=j:
                    prod=prod*nums[j]
            L.append(prod)

        return L
        