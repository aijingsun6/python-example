import json
from io import StringIO
s = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

print(s)

s = json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'))
print(s)

io = StringIO()
json.dump(['streaming API'], io)
s = io.getvalue()
print(s)

def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct


c = json.loads('{"__complex__": true, "real": 1, "imag": 2}',object_hook=as_complex)

print(c)

class ComplexEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, complex):
            return {"__complex__":True, "real": o.real,"imag":o.imag}
        # Let the base class default method raise the TypeError
        return super().default(o)


s = json.dumps(c,cls=ComplexEncoder)
print(s)
s = ComplexEncoder().encode(c)
print(s)