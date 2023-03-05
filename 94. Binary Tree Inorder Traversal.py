class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def tree(root):
            if not root:
                return None
            tree(root.left)
            res.append(root.val)
            tree(root.right)
        tree(root)
        return res

