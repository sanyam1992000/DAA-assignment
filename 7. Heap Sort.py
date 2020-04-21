# SANYAM MITTAL
# CE 42
# 18001003110

import sys
input = sys.stdin.readline


def multi_input():
    return map(int, input().split())


def array_print(array):
    print(' '.join(map(str, array)))


def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest = l

    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heapSort(array):
    n = len(array)

    for i in range(n//2-1, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # swap 
        heapify(array, i, 0)


array = list(multi_input())
heapSort(array)
print("Sorted array is")
array_print(array)
