from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class P1161:

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        max_sum = root.val
        max_depth = 1
        depth = 1
        q: list[TreeNode] = [root]
        while len(q) > 0:
            s2 = []
            s = 0
            for n in q:
                s += n.val
                if n.left is not None:
                    s2.append(n.left)
                if n.right is not None:
                    s2.append(n.right)
            if s > max_sum:
                max_depth = depth
                max_sum = s
            q = s2
            depth += 1
        return max_depth



import unittest

class P1161Test(unittest.TestCase):
    def test(self):
        n1 = TreeNode(val=1)
        n2 = TreeNode(val=7)
        n3 = TreeNode(val=0)
        n4 = TreeNode(val=7)
        n5 = TreeNode(val=-8)
        n1.left = n2
        n1.right = n3

        n2.left = n4
        n2.right = n5
        p = P1161()
        r = p.maxLevelSum(n1)
        self.assertEqual(2, r)

