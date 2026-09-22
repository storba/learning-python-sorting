import time
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

if __name__ == "__main__":
    evens = [2 * i for i in range(10000)]
    odds = [2 * i + 1 for i in range(10000)]

    shadow_merge(evens, odds)
    shadow_merge_2(evens, odds)
    # print(shadow_merge([1,3,5], [2,4,6]))
    # print(shadow_merge([1,2,3], [4,5,6]))
    # print(shadow_merge([1], [2,3,4]))
    # print(shadow_merge([], [1,2,3]))
    # print(shadow_merge([1,1,2], [1,3,3]))
    # print(shadow_merge([1,1,2], []))
    # print(shadow_merge([], []))