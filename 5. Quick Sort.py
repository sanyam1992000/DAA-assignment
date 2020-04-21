# SANYAM MITTAL
# CE 42
# 18001003110

import sys
input = sys.stdin.readline
def multi_input():
    return map(int, input().split())

def array_print(array):
    print(' '.join(map(str, array)))


def partition(array, low, high):
    i = (low - 1)
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i+1


def quickSort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quickSort(array, low, pivot - 1)
        quickSort(array, pivot + 1, high)


print("ENTER THE ARRAY TO BE SORTED")
array = list(multi_input())
n = len(array)

quickSort(array, 0, n - 1)

print("Sorted array is:")
array_print(array)
