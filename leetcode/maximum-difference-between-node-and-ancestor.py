# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:


        self.min = -1 
        self.max = 1_000_000
        self.ans = -1 
        def dfs(root, curMax, curMin): 

            if not root: 
                self.ans = max(self.ans, curMax-curMin)
                return 

            dfs(root.left, max(root.val,curMax), min(root.val, curMin))
            dfs(root.right, max(root.val,curMax), min(root.val, curMin))

        
        dfs(root, self.min, self.max)

        return self.ans