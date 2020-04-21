import sys
input = sys.stdin.readline
def multi_input():
    return map(int, input().split())

def array_print(arr):
    print(' '.join(map(str, arr)))

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def minKey(self, key, mstSet):
        min_index = 1
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index


    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [0] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)

print("Number of vertices (1-N)")
V = int(input())
g = Graph(V)
graph = [[0 for i in range(V+1)] for j in range(V+1)]
print("Number or edges")
e = int(input())
print("node1 node2 weight")
for i in range(e):
    n1 , n2, d = multi_input()
    graph[n1][n2] = d
    graph[n2][n1] = d

g.graph = graph
g.primMST()
