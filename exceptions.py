import sys
import traceback

class ExceptionOne(BaseException):
    def __init__(self,msg:str):
        self.msg = msg


def throws():
    raise Exception('exception origin')


def throws_one():
    try:
        throws()
    except BaseException as ex:
        tb = sys.exception().__traceback__
        one = ExceptionOne(msg=str(ex))
        one.with_traceback(tb)
        raise one

def main():
    try:
        throws_one()
    except BaseException as ex:
        es = traceback.format_exception(ex)
        for e in es:
            print(e)

if __name__ == '__main__':
    main()