# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:



        def buildBST(arr):

            if not arr: 
                return 

            mid = len(arr)//2 
            root = TreeNode(arr[mid]) 

            root.left = buildBST(arr[:mid])
            root.right = buildBST(arr[mid+1:])

            return root
        
        return buildBST(nums)

        # def buildBST(i,arr):

        #     if i >= len(arr): 
        #         return  

        #     root = TreeNode(arr[i]) 

        #     root.left = buildBST(i//2,arr[:i])
        #     root.right = buildBST(i//2, arr[i+1:])

        #     return root
        
        # return buildBST(len(nums)//2,  nums)

