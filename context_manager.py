import logging
import sys
logging.basicConfig(stream=sys.stdout,level=logging.INFO, format='%(asctime)s %(threadName)s %(taskName)s [%(levelname)s] - %(message)s')


class CMDemo(object):
    name:str
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        logging.info('CMDemo.__enter__ called')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        logging.info(f'CMDemo.__exit__,{exc_type}, {exc_val}, {exc_tb}')
        pass

    def hello(self):
        logging.info(f'CMDemo.hello: {self.name}')

# with CMDemo('cm') as cm:
#     cm.hello()

with CMDemo('cm') as cm:
    raise Exception('xyz')

class CMDemo2(object):
    cm: CMDemo
    def __init__(self, name):
        self.cm = CMDemo(name)

    def __enter__(self):
        logging.info('CMDemo2.__enter__ called')
        return self.cm

    def __exit__(self, exc_type, exc_val, exc_tb):
        logging.info(f'CMDemo2.__exit__,{exc_type}, {exc_val}, {exc_tb}')
        pass

    def hello(self):
        logging.info(f'CMDemo2.hello: {self.cm.name}')

# with CMDemo2('222') as cm:
#     logging.info(f'{type(cm)}')
#     cm.hello()