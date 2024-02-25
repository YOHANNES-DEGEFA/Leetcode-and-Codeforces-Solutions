# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:

     
        if not r1 and not r2: 
            return True 
        if (r1 and not r2) or (not r1 and r2) or (r1.val != r2.val):
            return False 
        return self.isSameTree(r1.left,r2.left) and self.isSameTree(r1.right,r2.right)


        