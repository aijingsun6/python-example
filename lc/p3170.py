class P3170:
    def clearStars(self, s: str) -> str:
        idx_buff : list[list[int]]= []
        for i in range(26):
            idx_buff.append([])

        remove = set()
        for idx in range(0, len(s)):
            c = s[idx]
            if c == '*':
                for aa in idx_buff:
                    if len(aa) == 0:
                        continue
                    remove.add(aa.pop())
                    break
            else:
                c2 = ord(s[idx]) - ord('a')
                idx_buff[c2].append(idx)

        res = ""
        for idx in range(0 ,len(s)):
            c = s[idx]
            if c == '*' or idx in remove:
                continue
            res += c
        return res

import unittest

class P3170Test(unittest.TestCase):
    def test_clearStars(self):
        s = 'aaba*'
        p = P3170()
        r = p.clearStars(s)
        self.assertEqual('aab',r)

        s = 'abc'
        r = p.clearStars(s)
        self.assertEqual('abc',r)


if __name__ == '__main__':
    unittest.main()
