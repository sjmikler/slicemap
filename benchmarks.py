import random
import time

from slicemap import SliceMap


def benchmark_insert_random(n=100):
    r = SliceMap()
    randoms = []
    for _ in range(n):
        a, b = sorted([random.random(), random.random()])
        randoms.append([a, b, random.random()])

    t0 = time.perf_counter()
    for a, b, v in randoms:
        r[a:b] = v
    print(time.perf_counter() - t0)


def benchmark_insert_range(n=100):
    r = SliceMap()
    numbers = []
    for i in range(n):
        a, b = (i, i + 1)
        numbers.append([a, b, random.random()])

    t0 = time.perf_counter()
    for a, b, v in numbers:
        r[a:b] = v
    print(time.perf_counter() - t0)
