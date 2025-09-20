def positional_only(posonly1, posonly2, /,**kwargs):
    print(posonly1, posonly2)

positional_only(1,2,**{})

def keyword_only(arg,*,foo,bar):
    print(arg,foo,bar)

keyword_only(1,foo=2,bar=3)

def var_positional(*args):
    print(args)

var_positional(1,2,3,4,5)


def var_keyword(**kwargs):
    print(kwargs)

var_keyword(foo=1,bar=2)