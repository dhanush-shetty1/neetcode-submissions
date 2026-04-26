from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp=defaultdict(int)
        mp[0]=1
        count=0
        curr=0

        for num in nums:
            curr+=num
            count+=mp[curr-k]
            mp[curr]+=1
        return count