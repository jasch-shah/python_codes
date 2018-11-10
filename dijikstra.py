from heapq import heappush, heappop

def read_graph(file):
	graph = dict()
	with open(file) as f:
		for l in f:
			(u, v, w) = l.split()
			if int(u) not in graph:
				graph[int(u)] = dict()
			graph[int(u)][int(v)] = int(w)
	return graph


inf = float('inf')
def dijikstra(graph, s):
	n = len(graph.keys())
	dist = dict()
	Q = list()

	for v in graph:
		dist[v] = inf
	dist[s] = 0
	
	heappush(Q, (dist[s], s))

	while Q:
		d, u = heappop(Q)
		if d < dist[u]:
			dist[u] = d 
		for v in graph[u]:
			if dist[v] > dist[u] + graph[u][v]:
				dis[v] = dist[u] + graph[u][v]
				heappush(Q, (dist[v], v))
	return dist		
	
graph = read_graph("graph.txt")
print dijikstra(graph, 1)								