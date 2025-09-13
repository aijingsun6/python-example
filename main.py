from bytesexample import a

a()


def mock_a():
    print('b')

import bytesexample
bytesexample.a = mock_a

bytesexample.a()