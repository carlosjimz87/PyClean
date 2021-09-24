import time


def classic_fib(limit):
    nums = []
    current, nxt = 0, 1

    while current < limit:
        nums.append(current)
        current, nxt = nxt, nxt + current

    return nums


def yield_fib(limit):
    current, nxt = 0, 1
    while current < limit:
        yield current
        current, nxt = nxt, nxt + current


N = 99
start_time = time.time()
fib = classic_fib(N)
print(f"Classic: {fib}")
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
fib = list(yield_fib(N))
print(f"Yielding: {fib}")
print("--- %s seconds ---" % (time.time() - start_time))
