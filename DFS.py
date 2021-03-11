from collections import defaultdict

def dfs_iterative(graph, start_vertex):
    visited = set()
    traversal = []
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal.append(vertex)
            stack.extend(reversed(graph[vertex]))   # add vertex in the same order as visited
    return traversal

graph = defaultdict(list)

n=int(input())


for i in range(n-1):
    u,v=[int(i) for i in input().split()]
    graph[u].append(v)
    
print(dfs_iterative(graph, 1))
