# creating class like this, allows to mute every properties of the class
# and every time you create a new property, new memory is created too

from collections import namedtuple
import time
import os
import inspect


def save(_data):
    filename = "out.txt"
    with open(filename, "w") as o:
        for d in _data:
            if inspect.isclass(d):
                print("{}".format(d.encode()), file=o)
            print("{}".format(d), file=o)

    return os.stat(filename).st_size / 1000


class RegularClass:
    def __init__(self, _a, _b, _c):
        self.a = _a
        self.b = _b
        self.c = _c


class SlottedClass:
    __slots__ = ['a', 'b', 'c']

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


# regular class
a = RegularClass(1, 2, 3)
b = RegularClass(1, 2, 3)

print(a.__dict__)
print(a.__dict__ == b.__dict__)
a.fun = True
print(a.__dict__)
print()

# slotted class
ai = SlottedClass(1, 2, 3)
bi = SlottedClass(1, 2, 3)

# ai.fun = True  # This FAILs because the only properties are the declared in the __slots__


# comparing memory to allocate in different kind of classes
N = 100_000
data = []
start_time = time.time()

# Case1: Tuples
print("Case1: Tuples")
for n in range(N):
    data.append((1 + n, 2 + n, 3 + n, 4 + n))

# Case2: Named Tuples
print("Case2: Named Tuples")
for n in range(N):
    nt = namedtuple('row', ['a', 'b', 'c'])
    data.append(nt(a=n + 1, b=n + 2, c=n + 3))

# Case3: Regular Class
print("Case3: Regular Class")
for n in range(N):
    obj = RegularClass(n+1, n+2, n+3)
    data.append(obj)

# Case4: Slotted Class
# ! THIS APPROACH RESTRICTS ALLOWED VALUES AND REMOVES PER INSTANCE DICT BACKING STORE
# ! BRINGING AS RESULT AND IMPROVED PERFORMANCE
print("Case4: Slotted Class")
for n in range(N):
    obj = SlottedClass(n + 1, n + 2, n + 3)
    data.append(obj)

delta = (time.time() - start_time) * 1000000
size = save(data)
print(f"--- {delta:.2f} ns --- {size:.2f} Kb")
