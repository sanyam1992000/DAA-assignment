# SANYAM MITTAL
# CE 42
# 18001003110

import sys
input = sys.stdin.readline
def multi_input():
    return map(int, input().split())

def array_print(array):
    print(' '.join(map(str, array)))


def binarySearch(array, left, right, x):
    if right >= left:
        mid = left + (right - left) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binarySearch(array, left, mid - 1, x)
        else:
            return binarySearch(array, mid + 1, right, x)
    else:
        return -1

print("Enter the array : ")
array  = list(multi_input())
array.sort()
print("Enter number to search")
x = int(input())
result = binarySearch(array, 0, len(array) - 1, x)

if result != -1:
    print("Element is present at index %d" % result)

else:
    print("Element is not present in array")




