class A:
    def __init__(self):
        pass

class B(A):
    def __init__(self):
        super().__init__()

a = A()
b = B()
print(isinstance(b, A))
print(issubclass(B, A))