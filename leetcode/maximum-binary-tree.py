# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        

        def heapfiy(s): 
            if not s: 
                return 

            i = s.index(max(s))
            root = TreeNode(s[i])

            root.left =  heapfiy(s[:i])
            root.right = heapfiy(s[i+1:])

            return root 
        return heapfiy(nums)