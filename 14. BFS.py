# SANYAM MITTAL
# CE 42
# 18001003110

import sys
input = sys.stdin.readline
def multi_input():
    return map(int, input().split())

def array_print(arr):
    print(' '.join(map(str, arr)))


print("Number of vertices")
V = int(input())
graph = {}

for i in range(1,V+1):
    graph[i] = []

print("Total number of edges")
edges = int(input())
print("Node 1 - Node 2")
visited = [0]*(V+1)

for i in range(edges):
    n1, n2 = multi_input()
    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(1,V+1):
    if visited[i]==0:
        stack = [i]
        visited[i] = 1
        while len(stack):
            node = stack.pop(0)
            print(node, end=' ')
            for i in graph[node]:
                if visited[node] == 0:
                    stack.append(i)
                    visited[node] = 1
