class Foo:
    age: int = 10

    def inc_age(self):
        self.age += 1

    def __str__(self):
        return "{}".format(self.age)


f1 = Foo()
f2 = Foo()
f1.inc_age()
f2.inc_age()
f2.age = 20
print(f1)
print(f2)
