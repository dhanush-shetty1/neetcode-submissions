# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans=0

        q=deque([root])

        while len(q)!=0:
            level=len(q)
            for i in range(level):
                e=q.popleft()
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
            
            ans+=1
        
        return ans
        