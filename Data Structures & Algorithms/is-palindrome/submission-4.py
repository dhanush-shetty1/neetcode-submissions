class Solution:
    def isAlpha(self,left,s):
        x=ord(s[left])
        if 97<=x<=142 or 48<=x<=57:
            return True
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        left=0
        right=len(s)-1

        while left<right:
            if not self.isAlpha(left,s):
                left+=1
                continue
            if not self.isAlpha(right,s):
                right-=1
                continue
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return False
        return True
            


        