a = bytes("12345", encoding="utf-8")
print(a)
b = bytes("abcde".encode("utf-8"))
print(b)
print(dir(b))
print(a+b)

