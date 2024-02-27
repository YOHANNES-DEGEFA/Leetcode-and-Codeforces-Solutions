# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []

        def inorderTraversal(root): 
            if not root: 
                return 
            inorderTraversal(root.left)
            arr.append(root.val)
            inorderTraversal(root.right)

        inorderTraversal(root)
        return arr == sorted(arr) and len(arr) == len(set(arr))
        