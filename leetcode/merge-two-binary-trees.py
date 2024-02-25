# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> Optional[TreeNode]:
 
        if not r1 and not r2: 
            return 
        if not r1: 
            r1 = r2 
            return r1 
        if not r2: 
            return r1 

        if r1 and r2: 
            r1.val +=r2.val  

        r1.left = self.mergeTrees(r1.left, r2.left)
        r1.right = self.mergeTrees(r1.right, r2.right)
       
        return r1