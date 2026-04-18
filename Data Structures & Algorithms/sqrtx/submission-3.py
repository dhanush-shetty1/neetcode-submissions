class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        low=0
        high=x//2

        while low<=high:
            mid=(high+low)//2

            if mid**2==x:
                return  mid
            elif mid**2>x:
                high=mid-1
            else:
                low=mid+1
        return high