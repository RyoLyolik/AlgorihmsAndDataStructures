from random import choice, random


def partition(array: list, l: int, r: int):
    x = array[l]  # pivot
    j = l
    for i in range(l + 1, r + 1):
        if array[i] <= x:
            j += 1
            array[j], array[i] = array[i], array[j]
    array[l], array[j] = array[j], array[l]
    return j


def quick_sort(array: list, l: int, r: int):
    if l < r:
        x = choice(range(l, r + 1))
        array[l], array[x] = array[x], array[l]
        pivot = partition(array, l, r)
        quick_sort(array, l, pivot - 1)
        quick_sort(array, pivot + 1, r)


# This version works bad if in array a lot of same elements
if __name__ == "__main__":
    n = 1000000
    array = [random() for i in range(n)]
    l, r = 0, len(array) - 1
    quick_sort(array, l, r)
    print(array == sorted(array))
