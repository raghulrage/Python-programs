'''Given a positive integer N. Consider a matrix of N X N. No cell can be accessible from any other cell, except the given pair cell in the form of (x1, y1), (x2, y2) i.e there is a path (accessible) between (x2, y2) to (x1, y1). The task is to find the count of pairs (a1, b1), (a2, b2) such that cell (a2, b2) is not accessible from (a1, b1).
''' 
def dfs(graph,visited, x, k): 
	for i in range(len(graph[x])): 
		if (not visited[graph[x][i]]): 
			
			# Incrementing the number of node 
			# in a connected component. 
			k[0] += 1

			visited[graph[x][i]] = True
			dfs(graph, visited, graph[x][i], k) 



# Inserting the edge between edge. 
def insertpath(graph, N, x1, y1, x2, y2): 
	
	# Mapping the cell coordinate 
	# into node number. 
	a = (x1 - 1) * N + y1 
	b = (x2 - 1) * N + y2 

	# Inserting the edge. 
	graph[a].append(b) 
	graph[b].append(a)

def countNonAccessible(graph, N): 
	visited = [False] * (N * N + N) 

	ans = 0
	for i in range(1, N * N + 1): 
		if (not visited[i]): 
			visited[i] = True
 
			k = [1] 
			dfs(graph, visited, i, k) 

			# Update result 
			ans += k[0] * (N * N - k[0]) 
	return ans 
# Driver Code 
if __name__ == '__main__': 

	N = 2

	graph = [[] for i in range(N*N + 1)] 

	insertpath(graph, N, 1, 1, 1, 2) 
	insertpath(graph, N, 1, 2, 2, 2) 

	print(countNonAccessible(graph, N)) 

