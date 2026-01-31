from typing import List

class P744:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters)
        while left < right:
            mid_idx = int((left + right) / 2)
            ch = letters[mid_idx]
            if ch > target:
                right = mid_idx
            else:
                left = mid_idx + 1
        if left >= len(letters):
            return letters[0]
        return letters[left]


import unittest

class P744Test(unittest.TestCase):
    def test(self):
        p = P744()
        letters = ['c', 'f', 'j']
        target = 'a'
        r = p.nextGreatestLetter(letters, target)
        self.assertEqual('c', r)

        letters = ['c', 'f', 'j']
        target = 'c'
        r = p.nextGreatestLetter(letters, target)
        self.assertEqual('f', r)

        letters = ['c', 'f', 'j']
        target = 'f'
        r = p.nextGreatestLetter(letters, target)
        self.assertEqual('j', r)

        letters = ["x","x","y","y"]
        target = 'z'
        r = p.nextGreatestLetter(letters, target)
        self.assertEqual('x', r)
