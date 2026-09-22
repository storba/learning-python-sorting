import time
import random

def timed(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

@timed
def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    res = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            res.append(list1[i])
            i+=1
        else:
            res.append(list2[j])
            j+=1
    while i < len(list1):
        res.append(list1[i])
        i+=1
    while j < len(list2):
        res.append(list2[j])
        j+=1
    return res

@timed
def shadow_merge_2(list1: list[int], list2: list[int]) -> list[int]:
    return sorted(list1 + list2)

def random_sorted(n, low=0, high=1000):
    arr = [random.randint(low, high) for _ in range(n)]
    arr.sort()
    return arr

if __name__ == "__main__":
    evens = [2 * i for i in range(10000)]
    odds = [2 * i + 1 for i in range(10000)]

    print("evens and odds")
    shadow_merge(evens, odds)
    shadow_merge_2(evens, odds)

    a = random_sorted(10000)
    b = random_sorted(10000)
    print("random sorted")
    shadow_merge(a, b)
    shadow_merge_2(a, b)