class Solution:
    def __init__(self):
        self.res = []

    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        self.res.append(root.val)
        if root.children:
            for child in root.children:
                self.preorder(child)
        return self.res
