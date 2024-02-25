# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def finder(root, val): 
            if not root: 
                return 
            if root.val < val: 
                return finder(root.right, val)

            elif root.val > val: 
                return finder(root.left, val)

            else: 
                return root
 

        return finder(root,val)