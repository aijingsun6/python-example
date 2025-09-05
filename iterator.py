"""
用来表示一连串数据流的对象。

重复调用迭代器的 __next__() 方法 (或将其传给内置函数 next()) 将逐个返回流中的项。 当没有数据可用时则将引发 StopIteration 异常。

到这时迭代器对象中的数据项已耗尽，继续调用其 __next__() 方法只会再次引发 StopIteration。

迭代器必须具有 __iter__() 方法用来返回该迭代器对象自身，因此迭代器必定也是可迭代对象，可被用于其他可迭代对象适用的大部分场合。 一个显著的例外是那些会多次重复访问迭代项的代码。

容器对象 (例如 list) 在你每次将其传入 iter() 函数或是在 for 循环中使用时都会产生一个新的迭代器。 如果在此情况下你尝试用迭代器则会返回在之前迭代过程中被耗尽的同一迭代器对象，使其看起来就像是一个空容器。


"""
import traceback
class MyIterator:
    data: list
    cursor:int
    def __init__(self, values:list):
        self.data = values
        self.cursor = 0

    def __iter__(self):
        self.cursor = 0
        return self

    def add_value(self,v):
        self.data.append(v)

    def __next__(self):
        if self.cursor < len(self.data):
            value = self.data[self.cursor]
            self.cursor += 1
            return value
        raise StopIteration()


if __name__ == '__main__':
    it = MyIterator([1,2,3])
    for e in it:
        print(e)
    print(it.cursor)
    its = iter(it)
    while True:
        try:
            print(next(its))
        except StopIteration as e:
            print(traceback.format_exception(e))
            break







