from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return 
        
        queue = deque()
        queue.append(root)
        res = []
        leftToRight = 0
        while queue:
            temp_queue = deque()
            temp_res = []
            while queue:
                node = queue.popleft()
                temp_res.append(node.val)
                
                if node.left: temp_queue.append(node.left)
                if node.right: temp_queue.append(node.right)
                
            if leftToRight %2 == 1:
                temp_res = temp_res[::-1]
            queue = temp_queue
            res.append(temp_res)
            leftToRight +=1
        return res

        
        