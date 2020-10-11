# normal
items = (1, 2)
items2 = (1, 2, 3, 4, 5)
print()
print(items)


# Unpacking both
a, b = items
print()
print(a)
print(b)


# Unpacking just one ignoring the other
a, _ = items
print()
print(a)

# Unpacking just one ignoring the rest
a, *_ = items2
print()
print(a)


# Unpacking some individually and some in a pack (safely)
a, b, *c = items2
print()
print(a)
print(b)
print(c)
