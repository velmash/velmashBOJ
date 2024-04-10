def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

cnt = 0

for _ in range(m):
    node, line = map(int, input().split())
    graph[node].append(line)

for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1

print(cnt)