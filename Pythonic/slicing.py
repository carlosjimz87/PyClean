import itertools
import time


def classic_fibo(limit):
    nums = []
    current, nxt = 0, 1

    while current < limit:
        nums.append(current)
        current, nxt = nxt, nxt + current

    return nums


def yield_fibbo(limit):
    current, nxt = 0, 1
    while current < limit:
        yield current
        current, nxt = nxt, nxt + current


N = 99
first5 = classic_fibo(N)[:5]
print(f"First 5 of classic fib: {first5}")
# first5 = classic_fibo(N)[:5] // TypeError because generator is not a iterable
first5 = list(itertools.islice(yield_fibbo(N), 5))
print(f"First 5 of yielding fib: {first5}")
