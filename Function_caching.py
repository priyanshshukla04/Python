import time
from functools import lru_cache
@lru_cache(maxsize=3)
def func(n):
    time.sleep(n)
    return n

if __name__=='__main__':
    print("Now running some work")
    func(3)
    func(1)
    func(6)
    func(2)
    print("Done... Calling again")
    input()
    func(3)
    print("Called again")
