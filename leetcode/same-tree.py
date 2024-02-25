# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def checker(r1, r2): 

            if not r1 and not r2: return True 
            if not r1 and r2: return False 
            if not r2 and r1: return False 

            if r1.val != r2.val: return False 

            return checker(r1.left,r2.left) and checker(r1.right,r2.right)

        return checker(p,q)


        


        
        