from random import choice, random


# import sys
# sys.setrecursionlimit(10001)

def partition(array: list, l: int, r: int):
    x = array[l]  # pivot
    m1 = l
    for i in range(l + 1, r + 1):
        if array[i] < x:
            m1 += 1
            array[m1], array[i] = array[i], array[m1]
    array[l], array[m1] = array[m1], array[l]
    m2 = m1
    for i in range(m1 + 1, r + 1):
        if array[i] == x:
            m2 += 1
            array[m2], array[i] = array[i], array[m2]

    return m1, m2


def quick_sort(array: list, l: int, r: int):
    if l < r:
        x = choice(range(l, r + 1))
        array[l], array[x] = array[x], array[l]
        pivot1, pivot2 = partition(array, l, r)
        quick_sort(array, l, pivot1 - 1)
        quick_sort(array, pivot2 + 1, r)


if __name__ == "__main__":
    n = 10000
    array = [random() for i in range(n)]
    l, r = 0, len(array) - 1
    quick_sort(array, l, r)
    print(array)
