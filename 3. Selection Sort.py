# SANYAM MITTAL
# CE 42
# 18001003110

import sys
input = sys.stdin.readline
def multi_input():
    return map(int, input().split())

def array_print(arr):
    print(' '.join(map(str, arr)))

print("ENTER ARRAY TO BE SORTED")
array = list(multi_input())

for i in range(len(array)):
    min_idx = i
    for j in range(i + 1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]

print("Sorted array")
array_print(array)