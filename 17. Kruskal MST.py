import sys
input = sys.stdin.readline
def multi_input():
    return map(int, input().split())

def array_print(arr):
    print('\n'.join(map(str, arr)))


def findparent(x,parent):
    if parent[x] != x:
        parent[x] = findparent(parent[x], parent)
    return parent[x]

def union(x,y,parent):
    x = findparent(x,parent)
    y = findparent(y, parent)
    parent[x] = y

def kruskal(edges, n):
    edges = sorted(edges, key=lambda item: item[2])
    counter = 0
    i = 0
    new_edges = []
    while counter < n-1:
        x = edges[i][0]
        y = edges[i][1]
        toll = edges[i][2]
        xparent = findparent(x, parent)
        yparent = findparent(y, parent)
        if xparent != yparent:
            counter += 1
            union(x, y, parent)
            print(edges[i])
        i +=1
    return new_edges


print("Number of Vertices ")
n = int(input())
print("Numer of edges")
nedges = int(input())
print("node1 node2 weight")
edges = []
for i in range(nedges):
    temp = list(multi_input())
    edges.append(temp)


parent = []
for i in range(n + 1):
    parent.append(i)

new = kruskal(edges, n)