# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        d = defaultdict(list)

        def dfs(root,i,h): 
            if not root: 
                return 
            
            dfs(root.left, i-1, h+1)
            dfs(root.right, i+1, h+1)
            d[i].append((root.val,h))


        
        dfs(root,0,0)
        def custComp(x): 
            return x[1], x[0]

        def sortAppend(d): 
            arr = sorted(d.keys())
            res = []

            for k in arr: 
                res.append(sorted(d[k], key=custComp))
            
            ans = []
            for lst in res: 
                tmp = []
                for a,b in lst: 
                    tmp.append(a)

                ans.append(tmp)


            return ans

        return sortAppend(d)
        