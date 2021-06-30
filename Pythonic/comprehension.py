# cloning a list
import math
nums = [1, 2, 3, 4]

# [print(x) for x in nums]
# duplicating items of a list
# new_nums = [math.sqrt(n) for n in nums]  # n*n = n**2
# print(new_nums)

# filtering even numbers of a list

# new_nums = [n for n in nums if n % 2 == 0]
# new_nums = filter(lambda n: n % 2 == 0, nums)
# print([n for n in new_nums])

# # merging items of a list with items of another list and getting pairs listed
# letters = 'abcd'

# new_pairs = [(letter, num) for letter in letters for num in nums]
# print(new_pairs)

# dictionary comprehensions
# create a dict from two zipped lists [filtering starting with 'S' heronames]
# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# new_dict = {name: hero for name, hero in zip(
#     names, heroes) if hero.startswith('S')}
# print(new_dict)

# set comprehensions
# create a set from list

new_set = {n for n in nums}
print(new_set)


# generator comprehensions
# generate squared items from a list of nums
new_gen_nums = (n*n for n in nums)
[print(i) for i in new_gen_nums]
