# SANYAM MITTAL
# CE 42
# 18001003110

import sys
input = sys.stdin.readline
def multi_input():
    return map(int, input().split())

def array_print(array):
    print(' '.join(map(str, array)))

def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

# Driver code to test above]
print("Enter array")
array = list(multi_input())

bubbleSort(array)

print("Sorted array is:")
array_print(array)