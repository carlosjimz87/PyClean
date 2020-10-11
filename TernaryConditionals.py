def withoutTernary(condition):
    if(condition):
        x = 1
    else:
        x = 0
    return x


def withTernary(condition):
    x = 1 if (condition) else 0
    return x


# print(withoutTernary(True))
print(withTernary(True))
