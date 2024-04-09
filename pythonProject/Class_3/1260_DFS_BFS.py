from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for adj in graph:
    adj.sort()


def dfs(v, visited=[]):
    visited.append(v)
    for i in  graph[v]:
        if i not in visited:
            dfs(i, visited)

    return visited

def bfs(v):
    queue = deque()
    queue.append(v)
    visited = []

    while queue:
        q = queue.popleft()
        visited.append(q)

        for i in graph[q]:
            if i not in visited and i not in queue:
                queue.append(i)

    return visited

for i in dfs(V):
    print(i, end=' ')
print()

for i in bfs(V):
    print(i, end=' ')
