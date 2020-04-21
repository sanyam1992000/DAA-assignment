# SANYAM MITTAL
# CE 42
# 18001003110

import sys
input = sys.stdin.readline
def multi_input():
    return map(int, input().split())

def array_print(arr):
    print(' '.join(map(str, arr)))

def shortest_path(parent, node, dist, graph, visited):
    if visited[node]==0 or distance[node]>distance[parent]+dist:
        distance[node] = distance[parent] + dist
        visited[node] = 1
        for curr_node in graph[node]:
            node1 = curr_node[0]
            d = curr_node[1]
            shortest_path(node, node1, d, graph, visited)


print("Number of vertices")
V = int(input())
graph = {}

for i in range(1,V+1):
    graph[i] = []

print("Total number of edges")
edges = int(input())
print("Node 1 - Node 2 - distance")
visited = [0]*(V+1)
distance = [0]*(V+1)

for i in range(edges):
    n1, n2, d = multi_input()
    graph[n1].append([n2,d])
    graph[n2].append([n1,d])

for i in range(1, V+1):
    if visited[i]==0:
        shortest_path(0, i, 0, graph, visited)

array_print(distance[1:V+1])
