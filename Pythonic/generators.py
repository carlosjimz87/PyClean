nums = [1, 2, 3, 4]


def squares(_nums):
    for n in _nums:
        yield n*n


squared_nums = squares(nums)

# print(next(squared_nums))
# print(next(squared_nums))
# print(next(squared_nums))
# print(next(squared_nums))

# or

for num in squared_nums:
    print(num)

# this resource has better resource optimization hence better performance
