class Node:
    def __init__(self,val:int):
        self.val=val
        self.right=None
        self.left=None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        

        def same(left,right):
            if left>right:
                return None
            
            mid=(left+right)//2
            root=TreeNode(nums[mid])

            root.left=same(left,mid-1)
            root.right=same(mid+1,right)

            return root
        
        return same(0,len(nums)-1)

