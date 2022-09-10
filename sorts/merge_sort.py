def merge_sort(array: list):
    n = len(array)
    if n > 1:
        left = merge_sort(array[:n // 2])
        right = merge_sort(array[n // 2:])
        array = merge(left, right)
        return array
    return array


def merge(array1: list, array2: list):
    res = []
    if len(array1) == 0:
        return array2
    if len(array2) == 0:
        return array1
    i, j = 0, 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            res.append(array1[i])
            i += 1
        else:
            res.append(array2[j])
            j += 1

    while i < len(array1):
        res.append(array1[i])
        i += 1

    while j < len(array2):
        res.append(array2[j])
        j += 1

    return res


if __name__ == "__main__":
    from random import random

    n = 100000
    arr = [int(random() * n) for _ in range(n)]
    x = merge_sort(arr)
    print(x == sorted(arr))
