# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        q=deque([root])
        flag=True
        def h(node):
            nonlocal flag
            if not node:
                return 0

            l=h(node.left)
            r=h(node.right)
            if abs(l-r)>1:
                flag=False
            return 1+max(l,r)
        
        h(root)
        return flag
        