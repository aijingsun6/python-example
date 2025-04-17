import logging

root = logging.getLogger()
print(root)

a = logging.getLogger("a")
print(a)

b = logging.getLogger("a.a")
print(b)