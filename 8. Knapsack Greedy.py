# SANYAM MITTAL
# CE 42
# 18001003110

import sys
input = sys.stdin.readline
def multi_input():
    return map(int, input().split())

def array_print(arr):
    print(' '.join(map(str, arr)))


class ItemValue:
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt

    def __lt__(self, other):
        return self.cost < other.cost


class FractionalKnapSack:
    @staticmethod
    def getMaxValue(wt, val, capacity):

        iVal = []
        for i in range(len(wt)):
            iVal.append(ItemValue(wt[i], val[i], i))

        iVal.sort(reverse=True)
        totalValue = 0

        for i in iVal:
            curWt = int(i.wt)
            curVal = int(i.val)
            if capacity - curWt >= 0:
                capacity -= curWt
                totalValue += curVal
            else:
                fraction = capacity / curWt
                totalValue += curVal * fraction
                capacity = int(capacity - (curWt * fraction))
                break
        return totalValue


print("Enter Weights")
wt = list(multi_input())
print("Enter Values")
val = list(multi_input())
print("Total Capacity")
capacity = int(input())

maxValue = FractionalKnapSack.getMaxValue(wt, val, capacity)
print("Maximum value in Knapsack = ", maxValue)
