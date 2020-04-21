# SANYAM MITTAL
# CE 42
# 18001003110

import sys
input = sys.stdin.readline
def multi_input():
    return map(int, input().split())

def array_print(array):
    print(' '.join(map(str, array)))


def merge(array, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    left = [0]*n1
    right = [0]*n2

    for i in range(0, n1):
        left[i] = array[left + i]

    for j in range(0, n2):
        right[j] = array[mid + 1 + j]

    i = j = 0 
    k = left

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = right[j]
        j += 1
        k += 1


def mergeSort(array, left, right):
    if left < right:
        mid = (left + (right - 1)) // 2
        mergeSort(array, left, mid)
        mergeSort(array, mid + 1, right)
        merge(array, left, mid, right)


array = list(multi_input())
n = len(array)
mergeSort(array, 0, n - 1)
print("Sorted array is")
array_print(array)
