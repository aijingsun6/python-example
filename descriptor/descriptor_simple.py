import logging
import sys

logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    format="%(asctime)s %(name)s %(levelname)s %(filename)s %(funcName)s %(message)s")
logger = logging.getLogger(__name__)


class Ten:
    def __get__(self, obj, objtype):
        logger.info("obj={}, objtype={}".format(obj, objtype))
        return 10


class A:
    x = 5  # 常规类属性
    y = Ten()


a = A()
logger.info(a)
logger.info(a.y)


class LoggedAgeAccess:

    def __get__(self, obj, objtype=None):
        value = obj._age
        logger.info('Accessing %r giving %r', 'age', value)
        return value

    def __set__(self, obj, value):
        logger.info('Updating %r to %r', 'age', value)
        obj._age = value


class Person:
    age = LoggedAgeAccess()  # 描述器实例

    def __init__(self, name, age):
        self.name = name  # 常规实例属性
        self.age = age  # 调用 __set__()

    def birthday(self):
        self.age += 1  # 调用 __get__() 和 __set__()


person = Person(name="foo", age=10)
logger.info(person.age)
person.age = 20
logger.info(person.age)


class LoggedAccess:

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        value = getattr(obj, self.private_name)
        logger.info('Accessing %r giving %r', self.public_name, value)
        return value

    def __set__(self, obj, value):
        logger.info('Updating %r to %r', self.public_name, value)
        setattr(obj, self.private_name, value)


class Person2(object):
    name = LoggedAccess()  # First descriptor instance
    age = LoggedAccess()  # Second descriptor instance

    def __init__(self, name, age):
        self.name = name  # Calls the first descriptor
        self.age = age  # Calls the second descriptor

    def birthday(self):
        self.age += 1


logger.info("------")
p = Person2(name="Alice", age=5)
logger.info(p)
logger.info(p.name)
