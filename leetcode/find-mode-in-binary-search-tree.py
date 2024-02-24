# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)

        def traverse(root): 
            if not root: return 

            freq[root.val] += 1 

            traverse(root.left)
            traverse(root.right)
        traverse(root)
        mode = max(freq.values())
        ans = []

        for k, v in freq.items(): 
            if v == mode: 
                ans.append(k)

        return ans

        