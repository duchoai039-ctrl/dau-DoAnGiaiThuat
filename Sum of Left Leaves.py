class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.countSum(root, False)
    def countSum(self, node, isLeft):
        if not node:
            return 0
        if not node.left and not node.right and isLeft:
            return node.val
        return self.countSum(node.left, True) + self.countSum(node.right, False)


        