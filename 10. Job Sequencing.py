# SANYAM MITTAL
# CE 42
# 18001003110

import sys
input = sys.stdin.readline
def multi_input():
    return map(int, input().split())

def array_print(array):
    print(' '.join(map(str, array)))


def printJobScheduling(array, t):
    n = len(array)

    for i in range(n):
        for j in range(n - 1 - i):
            if array[j][2] < array[j + 1][2]:
                array[j], array[j + 1] = array[j + 1], array[j]

    result = [False] * t
    job = ['-1'] * t

    for i in range(len(array)):
        for j in range(min(t - 1, array[i][1] - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                job[j] = array[i][0]
                break
    print(job)


print("Enter total Jobs")
n = int(input())
print(" Name  - Arrival Time - Exec Time")
array = []
for i in range(n):
    temp = list(multi_input())
    array.append(temp)

print("Following is maximum profit sequence of jobs")
printJobScheduling(array, 3)