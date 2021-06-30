# normal
# items = (1, 2)
# items2 = (1, 2, 3, 4, 5)
# print()
# print(items)


# # Unpacking both
# a, b = items
# print()
# print(a)
# print(b)


# # Unpacking just one ignoring the other
# a, _ = items
# print()
# print(a)

# # Unpacking just one ignoring the rest
# a, *_ = items2
# print()
# print(a)


# # Unpacking some individually and some in a pack (safely)
# a, b, *c = items2
# print()
# print(a)
# print(b)
# print(c)


def fun(*args, **kwargs):
    print("args=", args, "kwargs=", kwargs)


def fun2(arg1, arg2, *args, **kwargs):
    print("args1=", arg1, "args2=", arg2, "args=", args, "kwargs=", kwargs)


fun2(1, 2, 3, {'a': 3})
