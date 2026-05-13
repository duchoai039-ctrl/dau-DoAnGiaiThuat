# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        res = []

        def dfs(string,node):
            if not node:
                return

            if not node.left and not node.right:
                res.append(string+str(node.val))

            dfs(string+str(node.val)+"->",node.left)
            dfs(string+str(node.val)+"->",node.right)
        
        dfs("",root)

        return res
        