import concurrent.futures
import time 

def fun(chain):
    time.sleep(2)
    print(chain)

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(fun, range(3))