class Solution:
    def __init__(self):
        self.res = []

    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        if root.children:
            for child in root.children:
                self.postorder(child)
        self.res.append(root.val)
        return self.res


