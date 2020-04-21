# SANYAM MITTAL
# CE 42
# 18001003110

import sys
input = sys.stdin.readline
def multi_input():
    return map(int, input().split())


def array_print(arr):
    print(' '.join(map(str, arr)))


def lcs(X, Y):
    m = len(X)-1
    n = len(Y)-1
    dp = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


print("Enter the first string")
X = input()
print("Enter the second string")
Y = input()
print("Length of LCS is ", lcs(X, Y))

