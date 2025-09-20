import inspect
import typing
from dataclasses import dataclass


def sum_two_numbers(a: int, b: int) -> int:
   return a + b
print(inspect.get_annotations(sum_two_numbers))

def hello(a:int):
    print(a)
print(inspect.get_annotations(hello))


def hello_2(a:int,b: tuple[str,int]) -> list[str]:
    return []
d = inspect.get_annotations(hello_2)
for k,v in d.items():
    print(k,type(k), v, type(v))

print(typing.get_type_hints(hello_2))



class C:
    field_a: str
    field_b: int
    field_c: object
    field_d: any
    field_e: None

print(inspect.get_annotations(C))

print('------')


@dataclass
class A:
    name: str

    age: int

    def __init__(self):
        pass
    def hello(self, value:str):
        print(f'{self.name}: {self.age}')

a = A()
a_type = type(a)
print(inspect.get_annotations(a_type))
print(a.__dict__)
hello = a_type.hello
print(hello, type(hello))

print(inspect.get_annotations(hello))



