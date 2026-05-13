# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #check node1=None before calling io first time
        def io(node,ans=[]):
            if node.left:
                io(node.left,ans)
            ans.append(node.val)
            if node.right:
                io(node.right,ans)
            return ans
        if root:
            return io(root)
        return []
