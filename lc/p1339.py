from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class P1339:

    sum_list : list[int]
    def node_sum(self, root: TreeNode):
        res = root.val
        if root.left:
            res += self.node_sum(root.left)
        if root.right:
            res += self.node_sum(root.right)
        self.sum_list.append(res)
        return res

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.sum_list = []
        total = self.node_sum(root)
        gap_min = total
        num = total
        for item in self.sum_list:
            gap = abs(item - (total-item))
            if gap < gap_min:
                gap_min = gap
                num = item

        res = num * (total -num)
        return res % (10**9 + 7)


import unittest

class P1339Test(unittest.TestCase):

    def test(self):
        n1 = TreeNode(val=1)
        n2 = TreeNode(val=2)
        n3 = TreeNode(val=3)
        n4 = TreeNode(val=4)
        n5 = TreeNode(val=5)
        n6 = TreeNode(val=6)

        n1.left = n2
        n1.right = n3
        n2.left = n4
        n2.right = n5
        n3.left = n6

        p = P1339()
        r = p.maxProduct(n1)
        self.assertEqual(110, r)


    def test2(self):
        n1 = TreeNode(val=1)
        n2 = TreeNode(val=2)
        n3 = TreeNode(val=3)
        n4 = TreeNode(val=4)
        n5 = TreeNode(val=5)
        n6 = TreeNode(val=6)

        n1.right = n2
        n2.left = n3
        n2.right = n4
        n4.left = n5
        n4.right = n6

        p = P1339()
        r = p.maxProduct(n1)
        self.assertEqual(90, r)


