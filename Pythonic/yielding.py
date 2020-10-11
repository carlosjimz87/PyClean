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
start_time = time.time()
fib = classic_fibo(N)
print(f"Classic: {fib}")
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
fib = list(yield_fibbo(N))
print(f"Yielding: {fib}")
print("--- %s seconds ---" % (time.time() - start_time))
