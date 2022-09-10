def binary_search(array: list, x):
    l, r = 0, len(array)
    while l < r:
        m = (l + r) // 2
        if array[m] < x:
            l = m + 1
        else:
            r = m
    return l


def lower_binary_search(array: list, x):
    return binary_search(array, x)


def upper_binary_search(array: list, x):
    l, r = 0, len(array)
    while r - l > 1:
        m = (l + r) // 2
        if array[m] <= x:
            l = m
        else:
            r = m
    return l


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 4, 5, 5, 5, 6, 7]
    ind = upper_binary_search(arr, 3)
    print(ind, arr[ind])
