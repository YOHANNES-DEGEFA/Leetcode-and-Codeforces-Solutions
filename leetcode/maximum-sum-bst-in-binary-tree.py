# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.answer = 0   
        
        def dfs(root):
           
            if not root:
                return (0, float('+inf'), float('-inf'))
            
            left_sum, left_min, left_max = dfs(root.left)
            right_sum, right_min, right_max = dfs(root.right)
            
            if left_max < root.val < right_min:   # if the cur subtree is BSt 
                cur_sum = root.val + left_sum + right_sum     # add the left and right sum and store them as a cur_sum 

                if cur_sum > self.answer:   # maximize your answer 
                    self.answer = cur_sum 
                
                return (cur_sum, min(left_min, root.val), max(right_max, root.val))
            else:
                cur_sum = max(left_sum, right_sum)

                if cur_sum > self.answer: 
                    self.answer = cur_sum 

                return (cur_sum, float('-inf'), float('+inf'))
        
        ans = 0
        dfs(root)
        return self.answer

            