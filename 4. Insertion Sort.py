# SANYAM MITTAL
# CE 42
# 18001003110

import sys
input = sys.stdin.readline
def multi_input():
    return map(int, input().split())

def array_print(array):
    print(' '.join(map(str, array)))


def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


array = list(multi_input())
insertionSort(array)

print("Sorted array is:")
array_print(array)