import threading
import time

a = 1

def fun(chain):
    time.sleep(2)
    print(chain)

print(f"Sync:{a}")


# async thread
y = threading.Thread(target=fun, args=(f"Async:{a}",))
y.start()


# async daemon thread (run in background)
x = threading.Thread(target=fun, args=(f"Daemon:{a}",), daemon=True)
x.start()
x.join() # needed to wait for the daemon

a = 10

print(f"Sync:{a}")