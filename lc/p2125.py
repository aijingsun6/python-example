from typing import List
class Solution:

    def numberOfBeams(self, bank: List[str]) -> int:
        prev:int = 0
        res = 0
        for line in bank:
            r = self.devices(line)
            res += (prev * r)
            if r > 0:
                prev = r
        return res

    def devices(self, line:str):
        r = 0
        for e in line:
            if e == '1':
                r += 1
        return r

import unittest
class SolutionTest(unittest.TestCase):

    def test(self):
        s: Solution = Solution()
        bank = ["011001","000000","010100","001000"]
        r = s.numberOfBeams(bank)
        self.assertEqual(8,r)
