from dataclasses import dataclass
from typing import Optional

MATCH_ANY = "*"

@dataclass
class Node(object):
    match_key: str
    leaf: bool
    obj: any
    children: dict[str,any]
    size: int
    value: str


def parse_values(value: str) -> list[str]:
    values: list[str] = []
    arr = value.split("/")
    for e in arr:
        e = e.strip()
        if len(e) == 0:
            continue
        if e.startswith("{") and e.endswith("}"):
            e = MATCH_ANY
        values.append(e)
    return values

def dfs(n: Node, values: list[str], idx: int, acc:list):
    if idx == len(values):
        if n.leaf:
            acc.append(n)
        return

    p = values[idx]
    # 非最后一个节点
    if p in n.children:
        dfs(n.children[p], values, idx + 1, acc)
    if MATCH_ANY in n.children:
        dfs(n.children[MATCH_ANY], values, idx + 1, acc)

class MatchNode(object):
    root: Node

    def __init__(self):
        self.root = Node(match_key='',leaf=False,obj=None,children=dict(),size=0,value='')

    def add(self, value: str, obj: any):
        values = parse_values(value)
        n: Node = self.root
        for i in range(len(values)):
            p = values[i]
            if p in n.children:
                n = n.children[p]
            else:
                new_node = Node(match_key=p,leaf=False,obj=None,children=dict(),size=0,value='')
                n.children[p] = new_node
                n = new_node
        n.leaf = True
        n.obj = obj
        n.size = len(values)
        n.value = value


    def match(self, value: str) -> Optional[Node]:
        values = parse_values(value)
        acc = []
        dfs(self.root, values, 0, acc)
        if len(acc) == 0:
            return None

        res:Node = acc[0]
        for i in range(len(acc)):
            n = acc[i]
            if n.size > res.size:
                res = n
        return res


import unittest

class MatchNodeTest(unittest.TestCase):
    def test(self):
        match_node = MatchNode()
        match_node.add('/subject/37259117/',37259117)
        n = match_node.match('/subject/37259117/')
        self.assertEqual(37259117, n.obj)
        self.assertEqual('/subject/37259117/', n.value)

        match_node.add('/abc/{pid}/',37259117)
        n = match_node.match('/abc/37259117/')
        self.assertEqual(37259117, n.obj)
        self.assertEqual('/abc/{pid}/', n.value)

        match_node.add('/abc/{pid}/{pid}', 37259117)
        n = match_node.match('/abc/37259117/123')
        self.assertEqual(37259117, n.obj)
        self.assertEqual('/abc/{pid}/{pid}', n.value)
        pass


