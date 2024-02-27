# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.p, self.q = p.val, q.val
        if p.val > q.val: 
            self.p, self.q = self.q , self.p 
            
        def dfs(root): 
            if not root: 
                return 

            if root.val < self.p: 
                return dfs(root.right) 
            elif root.val > self.q: 
                return dfs(root.left)
            else: 
                return root

        return dfs(root)
            


        