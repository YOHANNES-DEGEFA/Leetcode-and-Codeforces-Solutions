# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:


        def calc(root, s): 

            if not root.left and not root.right: 
                return int(s+str(root.val))

            if not root.left: 
                return calc(root.right, s+str(root.val))
            if not root.right: 
                return calc(root.left, s+str(root.val))
            return calc(root.right, s+str(root.val)) + calc(root.left,s + str(root.val))


        return calc(root, '')