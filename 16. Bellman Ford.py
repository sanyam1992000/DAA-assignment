import sys
input = sys.stdin.readline
def multi_input():
    return map(int, input().split())

def array_print(arr):
    print(' '.join(map(str, arr)))


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printArr(self, dist):
        print("Vertex   Distance from Source")
        for i in range(self.V):
            print("% d \t\t % d" % (i, dist[i]))


    def BellmanFord(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0

        for i in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        self.printArr(dist)


print("Number of Vertices (1-N)")
V = int(input())
g = Graph(V)
print("Number of edges")
edges = int(input())
for i in range(edges):
    n1, n2, w = multi_input()
    g.addEdge(n1, n2, w)

g.BellmanFord(1)
