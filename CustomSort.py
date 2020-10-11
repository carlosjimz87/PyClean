from functools import cmp_to_key

# nums = [4, 3, 2, 1]
# sorted(nums, key=cmp_to_key(lambda a, b: a - b))
nums = [6, 4, 8, 2, 6, 9, 5, 7]
colors = ["red", "blue", "green", "violeta", "yellow", "cyan", "brown"]


def compare(c1, c2):
    return 1 if (c1) > (c2) else -1


snums = sorted(nums, key=cmp_to_key(compare))
print(snums)

# now using lambda
snums = sorted(nums, key=cmp_to_key(
    lambda c1, c2: 1 if c1 > c2 else -1))
print(snums)

# now using built-in function
scolors = sorted(colors, key=len)
print(scolors)
