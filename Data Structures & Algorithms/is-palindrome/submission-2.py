class Solution:
    def isAlpha(self,i,s):
        x=ord(s[i])
        if 97<=x<=122 or 48<=x<=57:
            return True
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        n=len(s)
        i,j=0,n-1

        while i<j:
            if not self.isAlpha(i,s):
                i+=1
                continue
            if not self.isAlpha(j,s):
                j-=1
                continue
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False
        return True
        
        

        
        