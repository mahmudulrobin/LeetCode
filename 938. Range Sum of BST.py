class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans=0
        def sum(root):
            if not root:
                return None
            if low<= root.val<=high:
                self.ans+=root.val
            if low<=root.val:
                sum(root.left)
            if high>=root.val:
                sum(root.right)
        sum(root)
        return self.ans
