# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        q = deque([[root,0,1]])   # root, level , 

        prevLevel, prevNum = 0, 1
        answer = 0 
        while q: 

            root, level, num = q.popleft()

            if level > prevLevel: 
                prevLevel = level 
                prevNum = num 

            answer  = max(answer, num - prevNum)
            if root.left: q.append([root.left, level+1, num*2])
            if root.right: q.append([root.right, level+1, num *2 + 1])

        return answer + 1


            

