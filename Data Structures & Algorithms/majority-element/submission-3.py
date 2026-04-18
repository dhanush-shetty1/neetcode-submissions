class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap={}
        mmax=0
        n=0
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1

        for num in nums:
            if hashmap[num]>mmax:
                mmax=hashmap[num]
                n=num
        return n
        