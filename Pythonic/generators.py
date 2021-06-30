nums = [1, 2, 3, 4]


def squares(nums):
    for n in nums:
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
