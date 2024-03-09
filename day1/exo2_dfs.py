graph = [[],[1, 1, 1, 1],[2, 1, 1, 1],[2, 1, 1, 1],[2, 1, 1, 1],[2, 1, 1, 1]]

visited = [False] * len(graph)


def dfs(graph, v, visited):
	visited[v] = True
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)
	return visited
    
            
print(dfs(graph,1,visited))



