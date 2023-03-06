class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode], sum=0) -> int:
        if not root:
            return 0
        sum = sum*2 + root.val
        if root.left or root.right:
            l = self.sumRootToLeaf(root.left, sum)
            r = self.sumRootToLeaf(root.right, sum)
            return l+r
        else:
            return sum

